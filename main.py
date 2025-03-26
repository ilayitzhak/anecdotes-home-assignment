from dummy_api import DummyApi

USERNAME = "emilys"
PASSWORD = "emilyspass"

def main():
    plugin = DummyApi(USERNAME, PASSWORD)
    plugin.run()

    # Test
    # if plugin.connectivity_test():
    #     print("Connected successfully!")
    #     collected_data = plugin.collect_evidence()
    #     print(collected_data)
    # else:
    #     print("Failed to connect.")

    # plugin_invalid = DummyApi(f"{USERNAME}123", f"{PASSWORD}123")
    # if plugin_invalid.connectivity_test():
    #     print("Connected successfully with invalid credentials!")
    # else:
    #     print("Failed to connect with invalid credentials.")

if __name__ == "__main__":
    main() 