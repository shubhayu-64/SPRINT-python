import speedtest

if __name__ == "__main__":
    print("Internet Speed Tester for Clinify-Open-Sauce by Shubhayu Majumdar\n")

    client = speedtest.Speedtest()
    print("Download Speed is: ", str(int(client.download())/(1024*1024)), "Mbps")
    print("Upload Speed is: ", str(int(client.upload())/(1024*1024)), "Mbps")
    print("Ping: ", client.results.ping)
