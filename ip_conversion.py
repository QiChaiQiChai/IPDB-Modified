import requests
import geoip2.database

# 用于从数据库中查找 IP 地址的地理位置
def get_geo_location(ip_address):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    try:
        response = reader.city(ip_address)
        country_code = response.country.iso_code
        # 这里你可以根据需要返回不同的地理位置信息，比如国家简称
        return country_code
    except:
        return None

# 读取在线文件并处理 IP 地址
def process_ip_urls(urls, output_file):
    with open(output_file, 'w') as f:
        for url in urls:
            response = requests.get(url)
            ips = response.text.split('\n')

            for ip in ips:
                ip = ip.strip()
                location = get_geo_location(ip)
                if location:
                    f.write(f"{ip}#{location}\n")
                else:
                    f.write(f"{ip}#Unknown\n")

if __name__ == "__main__":
    urls = [
        "https://example.com/ip_addresses1.txt",
        "https://example.com/ip_addresses2.txt",
        # Add more URLs as needed
    ]
    process_ip_urls(urls, "output.txt")
