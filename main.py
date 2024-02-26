import requests

def get_ips_from_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(f"Failed to fetch IPs from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching IPs from {url}: {e}")
    return []

def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            return data['countryCode']
    except Exception as e:
        print(f"Error fetching location for IP {ip}: {e}")
    return None

def convert_ips(input_urls, output_files):
    for input_url, output_file in zip(input_urls, output_files):
        ips = get_ips_from_url(input_url)  # 获取URL中的IP地址列表
        
        with open(output_file, 'w') as f:
            for ip in ips:
                location = get_location(ip)
                if location:
                    f.write(f"{ip}#{location}\n")
                else:
                    f.write(f"{ip}#Unknown\n")

if __name__ == "__main__":
    input_urls = ["https://ipdb.api.030101.xyz/?type=bestproxy", "https://ipdb.api.030101.xyz/?type=bestcf"]  # 包含IP地址的txt文件的多个URL
    output_files = ["bestproxy.txt", "bestcf.txt"]
    convert_ips(input_urls, output_files)
