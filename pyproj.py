############################################################################################################
#################################### Autotrader.co.uk Website Scraper#######################################
############################################################################################################
# Authors : Mohamed Essam SADEK & Mahmoud A'laa ISMAIL 
# Cloud Architecture track : INTAKE 41
# Do not forget to insert (shebang) >> #!/usr/bin/env python3

#Imports : Using requests, BeautifulSoup and pandas modules#####
#Using requests module to get the response of the accessed web pages
#Using BeautifulSoup module in order to analyze the html got using requests
#Using pandas module to facilitate the exporting '.csv' file
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Define Variables
#Ask user to enter a valid postal code
postcode = input("Please enter the postcode: ") 

#Ask user to enter a distance or enter 'National' to search all around UK
#Please read the Application sequence topic in the Manual carefully in this case
Distance = input ("Please enter the distance <National/ x miles>: ") 

Car_Model = []       #List of car models
Seller_Type = []     #List seller types
Primary_Phone = []   #List of primary contact number
Secondary_Phone = [] #List of secondary contact number

#Define Functions
'''
Name: Get_ContactNumber

input_param:BeautifulSoup object (bs_object)
            headers used in request.get()
            loop_var which a variable to loop on the objects in a single page

Output: returns a list of seller contact numbers

Function: This function gets the ID of each car from the soup object then 
it requests to get the full car details in json format after that,
it searches for the primary and secondadry contact numbers
with the specified key wanted ('07' and '0044' in this case)
'''
def Get_ContactNumber(bs_object, headers, loop_var):
    
    #Define variables
    contact_Numbers = ['NULL', 'NULL']

    #Get car ID from the soup object
    car_id = bs_object.find_all('li', attrs={ 'class' : 'search-page__result'})[loop_var].get('id')

    #Request to get all car details in json format
    phone_request = requests.get("https://www.autotrader.co.uk/json/fpa/initial/" + car_id, headers = headers)
    json_phone_request = phone_request.json()

    #Search for the priamary number
    primary_Number = json_phone_request['seller']['primaryContactNumber']
    #Filter the results to the specified keys
    primary_Number_check_1 = primary_Number.startswith("(07")
    primary_Number_check_2 = primary_Number.startswith("(0044")

    #Check whether the key is matching or not 
    if primary_Number_check_1 == True or primary_Number_check_2 == True :
        contact_Numbers[0] = primary_Number
    else:
        contact_Numbers[0] = 'NULL'

    #Some sellers do not have secondary contact number
    #This is an exception handling to this case, if the seller does not have a second number
    try:
        secondary_Number = json_phone_request['seller']['secondaryContactNumber']
        secondary_Number_check_1 = secondary_Number.startswith("(07")
        secondary_Number_check_2 = secondary_Number.startswith("(0044")
        #print ("Secondary number exists")  #For debugging purpose
    except KeyError:
        secondary_Number = 0
        secondary_Number_check_1 = False
        secondary_Number_check_2 = False
        #print("No secondary contact number") #For debugging purpose

    #Check whether the key is matching or not
    if secondary_Number_check_1 == True or secondary_Number_check_2 == True :
        contact_Numbers[1] = secondary_Number
    else:
        contact_Numbers[1] = 'NULL'
        
    #Return the list of numbers
    return contact_Numbers

'''
Name: ReFormat_Number

input: list of contact numbers

output: No output

Function: This function takes the unformated numbers then 
reformats the primary number and the secondary number (if exists)
'''

def ReFormat_Number(input_Numbers_list):

    #Check if the primary number matches the user prefered key
    if input_Numbers_list[0] != 'NULL':

        #Formating process
        primary_Mod_1 = input_Numbers_list[0].replace ("(","")
        primary_final_Mod = primary_Mod_1.replace(") ", "")

        #Adding contact number to the phone list
        Primary_Phone.append(primary_final_Mod)
    else:
        Primary_Phone.append('NULL')

    #Check if the secondary number matches the user prefered key
    if input_Numbers_list[1] != 'NULL':
        secondary_Mod_1 = input_Numbers_list[1].replace ("(","")
        secondary_final_Mod = secondary_Mod_1.replace(") ", "")

        #Adding contact number to the phone list
        Secondary_Phone.append(secondary_final_Mod)

    else:
        Secondary_Phone.append('NULL')

'''
Name: Create_csv
Input: file name
Output: No output
Function: This function creates a csv file
'''
def Create_csv(file_name):

    df = pd.DataFrame({'Car model':Car_Model,'Seller':Seller_Type,'Primary contact no.': Primary_Phone, 'Secondary contact no.': Secondary_Phone}) 
    df.to_csv( file_name +'.csv', index=False, encoding='utf-8')

#Define Headers 
headers = {
    "Cookie": "__cfduid=deaccbaa2ffeb51a6df7be2856d9cc5591609936157; abtcid=8f8cdeb0_994e_4def_8ed3_65f8db26645e; abTestGroups=FPA3T-ahI\
    -cmpT-cr1-hlI-bcI-rxI-smI-cfC-dpI-ctI-dfI-diI-d3I-fkT-ndT-fiI-gpC-iosellC-me2-mcI-nvT-nfT-npT-trI-nhT-orI-pxT-faT-search0I-xkI-spI\
    -dsI-lmI-uhT; bucket=desktop; sessVar=79cf32b0-7093-46a3-8b10-ec70e47f204c; userid=ID=aec9d898-d672-4cf7-8ee9-e4ad2517c7b4;\
    user=STATUS=0&HASH=93599d8b952aa787446c953ede96b66f&PR=&ID=aec9d898-d672-4cf7-8ee9-e4ad2517c7b4; GeoLocation=Town=&Northing=&\
    Latitude=51.556568272&Easting=&ACN=0&Postcode=E113LD&Longitude=0.0094344562; SearchData=postcode=E113LD; postcode=postcode=E113LD; \
    searches=; _at_sticky=\"2fb8dfcfbd936bc4\"; __cf_bm=ebf7dd3d553ff71d1e7d5efa1456f543f14d22f4-1609936158-1800-AbS1twokSp6whum3yFFJ1bSdJ7z5kOZGDpOSxa6Rg2\
    teCdyJFJQ5wepebgMWjsSl3f88zGmOeYPygeTPl3Nj9CQ=; cookiePolicy=seen.; _sp_ses.05b0=*; _sp_id.05b0=585924da-504d-43ed-a852-60334a6c827b.1609936159.1.1609936\
    702.1609936159.119df975-07d1-440e-b478-8039640094e3; utag_main=v_id:0176d7ac4108000aa6017d882f6b0104e00e300d0086e$_sn:1$_se:6$_ss:0$_st:1609937985568$ses_id:1609936158985%3Bexp-session$_pn:2%3Bexp-session$_prevpage:cars%3Asearch%3Aknown%3Aresults%3Bexp-1609939775438; AMCV_E4EF2A3F555B7FEA7F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C18634%7CMCMID%7C63351508211403304590281923135931661372%7CMCAAMLH-1610540959%7C6%7CMCAAMB-1610540959%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1609943359s%7CNONE%7CvVersion%7C2.4.0; sp=90125d36-73bf-40d6-86b9-a91de40fd4b5; AMCVS_E4EF2A3F555B7FEA7F000101%40AdobeOrg=1; model_5mintimestamp=Wed Jan 06 2021 14:29:20 GMT+0200 (Eastern European Standard Time); short_date=1/6/2021; ck_time=Wed Jan 06 2021 14:29:20 GMT+0200 (Eastern European Standard Time); prev_5minmodel_run=0; y6=2; AAMC_autouk_0=REGION%7C6; aam_uuid=63334430752775403500281340190514937881; LPCKEY-p-245=4b74b9e4-fc69-48f8-b2f3-07a01ce3b9069-50037%7Cnull%7CindexedDB%7C120; CAOCID=e4fdbfa2-1a2e-452c-b82f-3777ffe4cfab7-98800; osp_aam=sg%3D5835602; _gcl_au=1.1.1841389278.1609936162; _cs_ex=1535460044; _cs_c=0; cd_user_id=176d7ac4b3225a-0d059bf34918138-4c3f207e-100200-176d7ac4b33412; _ga=GA1.3.1298767535.1609936162; _gid=GA1.3.1117179749.1609936162; ki_t=1609936162493%3B1609936162493%3B1609936177520%3B1%3B2; ki_r=; ga_cid_cookie_val=1298767535.1609936162; _sp_enable_dfp_personalized_ads=true; _sp_v1_uid=1:991:957f2a39-5221-457b-a8df-215dc6f50a53; _sp_v1_data=2:199966:1609936164:0:2:-1:2:0:0:_:-1; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKBjLyQAyD2lidGKVUEDOvNCcHyC4BK6iurVWKBQAW54XRMAAAAA%3D%3D; _sp_v1_opt=1:login|true:last_id|11:; _sp_v1_consent=1!0:-1:-1:-1:-1:-1; _sp_v1_csv=null; _sp_v1_lt=1:; consentUUID=0ae46b6f-ff69-4a0a-aeed-e03ff46fe024; y39=1; _uetsid=cd8198e0501a11eb92fc29e23f010eca; _uetvid=cd81e890501a11eb991a97ab12700668; euconsent-v2=CO_mMRMO_mMRMAGABCENBHCgAP_AAH_AAAgwGMtX_T9bb2_je_Z999tkeYwf95y3p-wzhgeMs-8NyZeH_B4Wp2MyvBX4JiQKGRgEsjLBAQdlHGFcTQgAwIkViTLMYk2MjzNKJrJEilMbe2dYGD9vn8HT3ZCY70-_v__7v3ef_3oGLAEGAAKAQBC2AAIEChEIAAIQxAAAAACghAAoEkACRQALA4COUAAABAYAAQAAQAgoAIBAAIAAElAQAgBQIBAARAIAAQACAEAACAAgFgBICAAACgEhIARABCAAQQAAQchgQEABBAWGQEQAVABDACYAFwARwAywBqQD7APwAjABVwDeAJiATYAtEBbADAgGHjQAICmxEBgAFQAVgAuACGAGQAMsAagA2QB-AEAAIwAVcA1gB8gENgIvASIAmwBOwCkQFyAMCAYSAw8SADAAcAksBTYSB6AAgABYAFQAMgAcAA8ACIAFQAMAAagA8gCGAIoATIAqgCsAFgALgAbwA5gCGgEQARIAlgBNAClAGGAMgAZcA1ADVAGyAPiAfYB-gEAAIwASkAq4BfgDCAGKANYAbQA3ABvAD0AHyAQ2AioBF4CRAExAJlATYAnYBSICxQFsALkAXeAwIBgwDCQGGgMPCgAwAdgJLAU2EABADNAXkGgMgAqACsAFwAQwAyABlgDUAGyAPwAgABGACrgGsAN4AfIBDYCLwEiAJsATsApEBcgDAgGEgMPDgAwAHAJLAU2KgJAAqACGAEwALgAjgBlgDUAH4ARgAq4BvAEggJiATYAtgBcgDAgGHjoH4ACwAKgAZAA4ACKAGAAYgA1AB9AEMARQAmQBVAFYALAAXAAxABvADmAIYARAAlgBMACaAFGAKWAYQBhgDIAGiANQAbIA34B9gH4ARgAlIBVwCxAFzALqAXkAvwBhADFAG4gOmA6gB6AENgIiAReAkEBIgCbAE7AKaAVYAsWBbAFsgLgAXIAu0Bd4DBgGEgMNAYeAxIeADARUAksBTY4AIAA4AC4BGQD5EIEYACwAMgAiABiAEMAJgAVQAuABiADeAI4AYQA1ABvwD7APwAjABKQCrgF-AMIAYoA6gB6AEggJEATYApoBYoC0YFsAW0AuABcgC7QGHgMSIgAQFNkAAIBGSUCIABAACwAMgAcABFADAAMQAeABEACYAFUALgAYgA2gCGgEQARIAowBSgDCAGqANkAfgBGACrgF1AMUAbgA6gCLwEiAJsAWKAtgBdoDDyYAEBFRIAGABcAjIBPikC4ABYAFQAMgAcABFADAAMQAawBDAEUAJgAUgAqgBYAC4AGIAOYAhgBEACjAFKAMIAaIA1QBswD7APwAjABKQCrgFzALyAYQA2gBuAD0AIvASIAmwBOwCmgFbALFAWwAuABcgC7QGGgMPKgAwAfAJLAU2UABAAXAJEAA.YAAAAAAAAAAA; _fbp=fb.2.1609936186078.762307052; _tq_id.TV-18903627-1.0536=e4dc5c6418362267.1609936186.0.1609936186..", 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0", 
    "Connection": "close", 
    "Host": "www.autotrader.co.uk", 
    "Accept-Encoding": "gzip, deflate", 
    "Cache-Control": "max-age=0", 
    "Upgrade-Insecure-Requests": "1", 
    "Accept-Language": "en-US,en;q=0.5"
}

'''
user_choice = input('Welcome to the Autotrader scraper \n To search for a specific made, please enter '1' \n \
                     To scrap by a specific postalcode and radius please enter '2' ')

if user_choice == 1 :
    #Do the added task
elif user_choice == 2:
    #Do the written task
else:
    print ('Invalid Input. Run the program again') 
    exit()
'''

#Searching in all specified number of pages
first_page = 1 #The first page to search in
last_page = 30  #The last page to search in
for page_no in range (first_page, last_page):

    if Distance == 'National' :

        #The user wants to search in all over the country
        response = requests.get("https://www.autotrader.co.uk/car-search?advertClassification=standard&postcode=" + postcode + "&onesearchad=Used&onesearc\
        had=Nearly%20New&onesearchad=New&advertising-location=at_cars&is-quick-search=TRUE&exclude-delivery-option=on&page=" + str(page_no), headers = headers)

    else :
        #The user wants to search in a specified radius in miles
        response = requests.get("https://www.autotrader.co.uk/car-search?advertClassification=standard&postcode=" + postcode + "&radius=" + Distance +"&onesearchad=Use\
        d&onesearchad=Nearly%20New&onesearchad=New&advertising-location=at_cars&is-quick-search=TRUE&exclude-delivery-option=on&page=" + str(page_no), headers = headers)


    ############Using BeautifulSoup#######################
    #Get the BeautifulSoup object and save it in soup
    soup = BeautifulSoup(response.text, 'html.parser')

    #Searchnig in a single page
    first_obj = 1 #The first object in the page to search for
    last_obj = 11 #The last object in the page to search for

    for object_no in range (first_obj, last_obj) :

        #Get the contact number list without reformating
        Contact_List = Get_ContactNumber(soup, headers, object_no)

        #Check whether the seller contact numbers matches the user preference or not
        if Contact_List[0] != 'NULL' or Contact_List[1] != 'NULL':

            #Obtain the car model and add it to the car list
            Car_Model_var = soup.find_all('h3', attrs={'class' : 'product-card-details__title'})[object_no].get_text().strip()
            Car_Model.append(Car_Model_var)

            #Determine the seller type and add to the seller_type list
            Seller_Type_var = soup.find_all('div', attrs={'class' : 'product-card-seller__seller-type'})[object_no].get_text().split('-')[0].strip()
            Seller_Type.append(Seller_Type_var)

            #Reformatting the seller contact number
            ReFormat_Number(Contact_List)

        #Printing the progress of the searching process
        print('Scanning Page '+ str(page_no)+' object '+ str(object_no))

#Creating the csv file
Create_csv('autotrader')


    
