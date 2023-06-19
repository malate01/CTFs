import requests

def make_cookie(this_one):
	result = {}
	result['name']="%s" % this_one
	result['Created']="" # Insert appropriate date here
	result['Domain']="" # Insert appropriate domain here
	result['HostOnly']="true"
	result['HttpOnly']="false"
	result['Last Accessed']="" # Insert appropriate date here
	result['Path']="/"
	result['SameSite']="none"
	result['Secure']="false"
	result['Size']="5"
	return result

def main():
	for i in range(100):
		cookieToSend = make_cookie(i)

		url = 'http://example.com/search' # Update to appropriate domain and port

		r = requests.post(url,cookies=cookieToSend)

		print(r.text)
		choice = input("Continue to next? ('n' for no):")
		if (choice == 'n'):
			return
	
if __name__ == "__main__":
	main()
