from urllib import request
from os import system, makedirs

scan_downloader = """
███████╗ ██████╗ █████╗ ███╗   ██╗███████╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║██╔════╝    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║███████╗    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║╚════██║    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║███████║    ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝    ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
															by github.com/zeloww
"""

def getscans():
	headers = {
	"User-Agent": "Mozilla/50"
	}

	manga = input("What scans do you want? >>> ").replace(" ", "-")
	url = f"https://scansmangas.xyz/scans/{manga}/1/1.jpg"

	try:
		request.urlopen(request.Request(url, headers=headers)).read()

	except:
		print(f"[-] No scans found for {manga} !")
		return

	chapter_min = input("What minimum chapter do you want? [number] >>> ").lower()
	chapter_max = input("What maximum chapter do you want? [number/all] >>> ").lower()

	if chapter_min in ["a", "all"]:
		chapter_min = 1
		chapter_max = float("inf")

	elif chapter_max in ["a", "all"]:
		chapter_max = float("inf")

	else:
		chapter_min = int(chapter_min.replace("0", "1"))
		chapter_max = int(chapter_max)


	while chapter_min-1 < chapter_max:

		try:
			url = f"https://scansmangas.xyz/scans/{manga}/{chapter_min}/1.jpg"
			request.urlopen(request.Request(url, headers=headers)).read()
			page_number = 1

			while True:
				try:
					url = f"https://scansmangas.xyz/scans/{manga}/{chapter_min}/{page_number}.jpg"
					page = request.urlopen(request.Request(url, headers=headers)).read()
					print(url)
					page_number += 1

					makedirs(f"{manga}/{chapter_min}/", exist_ok=True)
					with open(f"{manga}/{chapter_min}/{manga}_{page_number}.jpg","wb") as file:
						file.write(page)

				except:
					break

		except:
			print(f"[-] Chapter {chapter_min} not found !")
			break

		if chapter_max != float("inf"):
			chapter_min += 1

	print(f"\nSuccessfully downloaded {manga} of {chapter_min-2} at {chapter_max}")

def main():
	while True:
		system("cls")
		system("color d")

		print(scan_downloader)
		getscans()

		restart = input("Do you want restart? [y/n]")
		if restart.lower() not in ["y", "yes"]:
			break

	exit("Bye :D")

main()