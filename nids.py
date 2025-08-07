import streamlit as st
import requests
import pandas as pd

API_KEY = "31NlE0ypCjXV5NW0zGJmNsQSPFYKfmGYhWWOY41EpfCA"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/2f7e90b9-b3f6-4a2d-8635-ba3d37969f59/predictions?version=2021-05-01"

def get_token(api_key):
    response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json().get("access_token")

def predict(input_data):
    token = get_token(API_KEY)
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}
    payload = {
        "input_data": [{
            "fields": list(input_data.columns),
            "values": input_data.values.tolist()
        }]
    }
    response = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)
    return response.json()

st.title("🚨 Intrusion Detection - Minimal Demo")
st.write("Just testing with essential inputs + dummy padding")

duration = st.number_input("Duration", value=0)
protocol_type = st.selectbox("Protocol Type", ["tcp", "udp", "icmp"])
service = st.text_input("Service", "http")
flag = st.text_input("Flag", "SF")
src_bytes = st.number_input("Source Bytes", value=100)
dst_bytes = st.number_input("Destination Bytes", value=50)

if st.button("Predict"):
    # Dummy values for the rest (just placeholders for now)
    dummy_values = [
        0,  # land
        0,  # wrong_fragment
        0,  # urgent
        0, 0, 1, 0, 0, 0, 0, 0,  # hot to su_attempted
        0, 0, 0, 0, 0, 0,        # rest of numerical fields
        0, 0,                   # is_host_login, is_guest_login
        1, 1, 0.0, 0.0, 0.0, 0.0,  # count to srv_rerror_rate
        0.0, 0.0, 0.0, 0, 0,  # same_srv_rate to dst_host_srv_count
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0  # final few fields
    ]

    input_values = [
        duration, protocol_type, service, flag, src_bytes, dst_bytes
    ] + dummy_values

    all_columns = [
        "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
        "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised",
        "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells",
        "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count",
        "srv_count", "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate",
        "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
        "dst_host_rerror_rate", "dst_host_srv_rerror_rate"
    ]
    print("Number of input values:", len(input_values))
    print("Number of column labels:", len(all_columns))
    print("All Columns:\n", all_columns)
    print("Input Values:\n", input_values)
    input_values = input_values[:41]  # truncate to match columns
    df = pd.DataFrame([input_values], columns=all_columns)

    try:
        result = predict(df)
        pred = result["predictions"][0]["values"][0][0]
        prob = result["predictions"][0]["values"][0][1]
        st.success(f"Prediction: {pred}")
        st.info(f"Confidence: {max(prob)*100:.2f}%")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
        st.json(result)  # optional: show raw response
