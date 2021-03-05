import http.client
import json 

# conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")
# headers = {
#     'x-rapidapi-host': "quotes15.p.rapidapi.com",
#     'x-rapidapi-key': "7d843f2983mshdc84105d5371ad9p10ab4fjsn70ab8bf4f812"
#     }


conn = http.client.HTTPSConnection("api.quotable.io")


def text():
	conn.request("GET", "/random")

	res = conn.getresponse()
	data = json.loads(res.read().decode("utf-8"))

	# print(data)

	content = data["content"]
	name = data["author"]
	quotes = content + "\n\t-"+name
	return quotes
