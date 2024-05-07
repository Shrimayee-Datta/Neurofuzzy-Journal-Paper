import numpy as np

def anomaly_detection(data, sigma_threshold=5):
    '''Detects anomalies in the dataset provided using the sigma rule and the provided threshold.'''
    sigma = np.std(data)
    mean = np.mean(data)
    anomalies = []
    for i in range(len(data)):
        if abs(data[i] - mean) > sigma_threshold * sigma: 
            anomalies.append(data[i])
    return anomalies, data

def test_anomaly_detection():
    '''
    Tests the anomaly detection function.
    '''
    data = list(np.random.randn(1000)) 
    data.append(10)  # Appending 10 as an anomaly
    anomalies, complete_data = anomaly_detection(data)
    print("Anomalies detected:", anomalies)
    print("Complete dataset with appended 10:", complete_data)

test_anomaly_detection()
