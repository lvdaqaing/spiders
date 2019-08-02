# 使用自造的cookies登录GitHub

import requests
from lxml import etree

str_1 = '_octo=GH1.1.518803230.1537264616; logged_in=no; _ga=GA1.2.102113046.1537264618; _gh_sess=SmJXdy8xaFB1WEhURGR5dzAvV2t6Z0tsYTNIcU1zaEcraFhDZXFIdk14RnNweWU2RWVwa2NhREZVa2xFdWRDR3JjYXdhSWdWYnJIWVVIU0ZzU2pxL1dNUTZKNTYvUWROdXc3ZW1EeUZVS1NNT3dQNW4xZVAzYUNwSFRvZTNlQ0tZbXZlVU5vaGFQQmJOWU5WRVVuWW4xN0FCRnQrSzVCcUlTbnl4N1dKN1UweGxWb3BjUGFpRUV4VGVvTUo0L1dkdEROSnR1bk90UTZDb2g1YXhlQUI2M1ZQeUtsb1FHSGc4dllMWVZjMTlRN3pDVFk1UE9jTEl3WWhhU1ExNVdhL2FJVGNYK2tod0FENm8ycGpoSkJlRXBIaUtXQU9JVlNwMlhYWkN5eXlaWmZZTzU3aWFkVkRIRm9pa0huVm5pV1U4TEFNTU9uV1ZQeWZsSUZ0OWNwWG1WUXcrbCtaZlRuVWpNZUVaVXJMR09aSVFGWXpQaTFnWVRjNXpycGhIbHBvM3VoV0F5b1p5TmdTcWxPSzRid21SWWxRM0hua3VrdGpvVlJqZ0h1YmNKamdCL0NLL3p2RXRRTjl1RVFQd1lKVS0tc2pFakpPYitKSzdTVXd4Q0pvV0pFdz09--c65f8a900a92f1372cfe65ea65a16a5a8daad995; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1'

str = '_octo=GH1.1.518803230.1537264616; logged_in=no; _ga=GA1.2.102113046.1537264618; _gh_sess=RTIralVlQ1pHaG0vVG44b3NsV0s4Z2VZTTVibUNPYXVXUlZTZFY3ZXoxRkRrbm1ENkQ1b2lhS0thdHJqVjMvSE9lbXpVYnZ2Y0tlUXFLeG1qREdVRWY5QW9jSEl1ZTZNeWpvbnpPeTVBenlaMUJoUk1WaHVRS3ZpdGRGbzlsZU55VUFZOFpFZWx3MXhkdGJCSEdRNy9DLzd1V2RFclhPa0ZkQzFYN0MveFQ3ZDR4dGFlSDZQVHRucTJmazBjNFB4VnR2K1NZOER4dXpBcTJhazJ1bG13Q3hHMFc5K2N2emJSSEhJYk5ZMHlNaGtxU2NRTXQwdERKQTBTemg5enFSOHRPMCsrdjdNRmtUQ2lHdm1qWVdVS2RXR0h0QnZXT1BFVDgzRlNTTW9GUjRuYXFyMmJsMXE5QkgwcEJTaldLTUgwZEZVVEMwRS9yVU1NdUQrVDB3YmRhV0IxdW95OWZjUkVSdFhLcTM5a3NYMWlzODM2c1BEVnZueW5WSjlPWXhFRno5RWJIaFc1RXRlL2RPeXlSUkpabEo4TTIzNEUyQnk1VGRESzg0ZnNCcz0tLXllS2Vua1k1RkFiZUtoRGdnakh1K3c9PQ%3D%3D--36a2f99aff599e48d249745eb062081c61205f28; tz=Asia%2FShanghai; has_recent_activity=1; _gat=1'

str_list = str.split(';')

# print(str_list)

# cookies = {}
#
# for item in str_list:
#     # print(item)
#     key = item.split('=')[0].strip()
#     value = item.split('=')[1].strip()
#     cookies[key] = value
# print(cookies)

cookies = {'__Host-user_session_same_site': 'c6fASxAkR3aPrLZByiXjBzRti2I39tEPdU_xWXzGrqg6pfdB', '_gh_sess': 'ZzI1WUxYNzZHcGdxYXdHanV0bDJhOE82UXUrenJvZzArUFVaMTlTd20zbDB0R0E1cUg0Rk1BcFVFUmZLdmRrVjUrTTRDL1IvMHVKUUlWZ1hUay9nRGV4ekRiRE1TVytqZXdTTklmSHplaGxCTStrUzg4RTI2UEVPZE5WVWFIMGRLdWgxU3ZyM3R3aFRTcVN0UG94MnkrWmxNZis3VFpHZnZ2TkdpeDVRVXpNNE1uNlZCdUIvWFdQWGVWSUx5NFhxLS0rakVTVWFFY1pYVnZPT0xCQWF0bW13PT0%3D--27f33cb73ecd41fe3a33c17918aec6dc1faf9283', 'has_recent_activity': '1', 'user_session': 'c6fASxAkR3aPrLZByiXjBzRti2I39tEPdU_xWXzGrqg6pfdB'}

# str = "{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Referer': 'https://github.com/', 'Host': 'github.com', 'Cookie': 'logged_in=yes; _octo=GH1.1.590245834.1540697897; dotcom_user=iamseancheney; _gh_sess=UFM1OVhFak5VamVaelBEcFcxdXVPU1lyUWoyQnFmWG5JbXBOUkJMTWhkWDZTODMxV1gzRDNPU3NMVEduNFZzTUI4bWJucEwyWU80aE5KSkJ6ZzI1TnJxaEpPamhoaU9KSUNUUmliNzJDTFVianJhTHJGVnZlM1FQMW11eEhRRTltWEY3c1BzQ3NTZTVYOHFlWVNjUFk0bWU5UGNJSHJhNVhMTWg1Q0pKS1VNS0FiY2Qwcnl5RWJ4OWhTY2l6Tzd5eWZjK2NkQlF1a2tEdFdLNVJRSDZLQjV6a3c4NmhnMDNPdmpBYUpKVkgvVT0tLVZoejFJNHdzQTYwd1Rmdk1MYWtxeEE9PQ%3D%3D--57f4467670177e45c92c01f0ae48433463705fc0; has_recent_activity=1; user_session=NaECyppFbMT826KtZh4-zSpFUOgPDYpmlzdIWYWfvZISeTFi; __Host-user_session_same_site=NaECyppFbMT826KtZh4-zSpFUOgPDYpmlzdIWYWfvZISeTFi'}"

header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

logined_url = 'https://github.com/settings/profile'
response = requests.get(logined_url, headers=header, cookies=cookies)
print(response.status_code)
print(response.text)
print(response.url)

tree = etree.HTML(response.text)

logo_url = tree.xpath('//dl[contains(@class,"form-group")]/dd/img/@src')[0]
print('logo url is:', logo_url)