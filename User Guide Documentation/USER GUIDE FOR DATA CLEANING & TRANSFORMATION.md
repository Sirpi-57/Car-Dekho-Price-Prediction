# **USER GUIDE FOR DATA CLEANING AND TRANSFORMATION**

# DATASET ANALYSIS:

The Dataset Consist of 6 Cities Used Card Data and it is given as an Excel File. It is in Unstructured Format and needs to be converted to Structured Format before proceeding to cleaning the data. Every City Data is similar so here we will see one in detail and the same has to be repeated for the other 5 as well.

## 1.Understanding the Unstructured Format:

The Data Consist of 5 Columns:  
                         1\. new\_car\_detail  
                         2\. new\_car\_overview  
                         3\. new\_car\_feature  
                         4\. new\_car\_specs  
                         5\. car\_links 

### **1.new\_car\_detail:**

Sample: {'it': 0, 'ft': 'Petrol', 'bt': 'SUV', 'km': '20,000', 'transmission': 'Automatic', 'ownerNo': 1, 'owner': '1st Owner', 'oem': 'Kia', 'model': 'Kia Sonet', 'modelYear': 2022, 'centralVariantId': 8654, 'variantName': 'Turbo DCT Anniversary Edition', 'price': '₹ 11.50 Lakh', 'priceActual': '', 'priceSaving': '', 'priceFixedText': None, 'trendingText': {'imgUrl': 'https://stimg.cardekho.com/used-cars/common/icons/trending.svg', 'heading': 'Trending Car\!', 'desc': 'High chances of sale in next 6 days'}}

It is a Nested Dictionary with a Dictionary inside a Dictionary. (2 Layers)

### **2\. new\_car\_overview:**

Sample: {'heading': 'Car overview', 'top': \[{'key': 'Registration Year', 'value': '2022', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/registrationYear.svg'}, {'key': 'Insurance Validity', 'value': 'Third Party insurance', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/insuranceValidity.svg'}, {'key': 'Fuel Type', 'value': 'Petrol', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/fuel.svg'}, {'key': 'Seats', 'value': '5 Seats', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/seats.svg'}, {'key': 'Kms Driven', 'value': '20,000 Kms', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/kmsDriven.svg'}, {'key': 'RTO', 'value': 'TN02', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/rto.svg'}, {'key': 'Ownership', 'value': 'First Owner', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/ownership.svg'}, {'key': 'Engine Displacement', 'value': '998 cc', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/engineDisplacement.svg'}, {'key': 'Transmission', 'value': 'Automatic', 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/transmission.svg'}, {'key': 'Year of Manufacture', 'value': 2022, 'icon': 'https://images10.gaadi.com/listing/vdp/co/v1/yearManufacture.svg'}\], 'bottomData': None}

Here it is Complex Nested Dictionary with A List of Dictionary inside a Dictionary within another Dictionary.(3 Layers)

### **3.new\_car\_feature:**

Sample: {'heading': 'Features', 'top': \[{'value': 'Power Steering'}, {'value': 'Power Windows Front'}, {'value': 'Air Conditioner'}, {'value': 'Heater'}, {'value': 'Adjustable Head Lights'}, {'value': 'Fog Lights Front'}, {'value': 'Anti Lock Braking System'}, {'value': 'Brake Assist'}, {'value': 'Radio'}\], 'data': \[{'heading': 'Comfort & Convenience', 'subHeading': 'Comfort', 'list': \[{'value': 'Power Steering'}, {'value': 'Power Windows Front'}, {'value': 'Power Windows Rear'}, {'value': 'Low Fuel Warning Light'}, {'value': 'Accessory Power Outlet'}, {'value': 'Trunk Light'}, {'value': 'Rear Reading Lamp'}, {'value': 'Rear Seat Headrest'}, {'value': 'Rear Seat Centre Arm Rest'}, {'value': 'Cup Holders Rear'}, {'value': 'Multifunction Steering Wheel'}, {'value': 'Cruise Control'}, {'value': 'Rear ACVents'}, {'value': 'Smart Access Card Entry'}, {'value': 'Engine Start Stop Button'}, {'value': 'Steering Wheel Gearshift Paddles'}, {'value': 'Battery Saver'}, {'value': 'Drive Modes'}, {'value': 'Remote Engine Start Stop'}, {'value': 'Adjustable Headrest'}\]}, {'heading': 'Interior', 'subHeading': 'Interior', 'list': \[{'value': 'Air Conditioner'}, {'value': 'Heater'}, {'value': 'Adjustable Steering'}, {'value': 'Digital Odometer'}, {'value': 'Electronic Multi Tripmeter'}, {'value': 'Leather Seats'}, {'value': 'Fabric Upholstery'}, {'value': 'Leather Steering Wheel'}, {'value': 'Glove Compartment'}, {'value': 'Digital Clock'}, {'value': 'Driving Experience Control Eco'}, {'value': 'Height Adjustable Driver Seat'}, {'value': 'Leather Wrap Gear Shift Selector'}\]}, {'heading': 'Exterior', 'subHeading': 'Exterior', 'list': \[{'value': 'Adjustable Head Lights'}, {'value': 'Fog Lights Front'}, {'value': 'Power Adjustable Exterior Rear View Mirror'}, {'value': 'Electric Folding Rear View Mirror'}, {'value': 'Rear Window Defogger'}, {'value': 'Alloy Wheels'}, {'value': 'Integrated Antenna'}, {'value': 'Tinted Glass'}, {'value': 'Rear Spoiler'}, {'value': 'Sun Roof'}, {'value': 'Moon Roof'}, {'value': 'Outside Rear View Mirror Turn Indicators'}, {'value': 'Chrome Grille'}, {'value': 'Roof Rail'}, {'value': 'LEDDRLs'}, {'value': 'LEDHeadlights'}, {'value': 'LEDTaillights'}\]}, {'heading': 'Safety', 'subHeading': 'Safety', 'list': \[{'value': 'Anti Lock Braking System'}, {'value': 'Brake Assist'}, {'value': 'Centeral Locking'}, {'value': 'Power Door Locks'}, {'value': 'Child Safety Locks'}, {'value': 'Driver Air Bag'}, {'value': 'Passenger Air Bag'}, {'value': 'Side Air Bag Front'}, {'value': 'Day Night Rear View Mirror'}, {'value': 'Passenger Side Rear View Mirror'}, {'value': 'Rear Seat Belts'}, {'value': 'Seat Belt Warning'}, {'value': 'Vehicle Stability Control System'}, {'value': 'Traction Control'}, {'value': 'Adjustable Seats'}, {'value': 'Keyless Entry'}, {'value': 'Engine Check Warning'}, {'value': 'Crash Sensor'}, {'value': 'Automatic Head Lamps'}, {'value': 'Ebd'}, {'value': 'Follow Me Home Headlamps'}, {'value': 'Rear Camera'}, {'value': 'Anti Pinch Power Windows'}, {'value': 'Speed Sensing Auto Door Lock'}, {'value': 'Isofix Child Seat Mounts'}, {'value': 'Pretensioners And Force Limiter Seatbelts'}, {'value': 'Hill Assist'}, {'value': 'Impact Sensing Auto Door Lock'}, {'value': 'No Of Airbags'}, {'value': 'Eletronic Stability Control'}\]}, {'heading': 'Entertainment & Communication', 'subHeading': 'Entertainment', 'list': \[{'value': 'Radio'}, {'value': 'Speakers Front'}, {'value': 'Speakers Rear'}, {'value': 'Integrated2Din Audio'}, {'value': 'Bluetooth'}, {'value': 'Touch Screen'}, {'value': 'Number Of Speaker'}, {'value': 'Apple Car Play'}, {'value': 'Android Auto'}\]}\], 'commonIcon': 'https://stimg.cardekho.com/pwa/img/vdpN/tickG.svg'}

Here it is even more Complex with a Dictionary inside a List inside another list inside another dictionary within another Dictionary. (5 Layers)

### **4.new\_car\_specs:**

Sample: {'heading': 'Specifications', 'top': \[{'key': 'Engine', 'value': '998 CC'}, {'key': 'Max Power', 'value': '118.36bhp'}, {'key': 'Torque', 'value': '172nm'}, {'key': 'Wheel Size', 'value': '16'}, {'key': 'Seats', 'value': '5'}\], 'data': \[{'heading': 'Engine and Transmission', 'subHeading': 'Engine', 'list': \[{'key': 'Color', 'value': 'Black'}, {'key': 'Engine Type', 'value': 'Smartstream G1.0 T \- GDi'}, {'key': 'Displacement', 'value': '998'}, {'key': 'Max Power', 'value': '118.36bhp@6000rpm'}, {'key': 'Max Torque', 'value': '172nm@1500-4000rpm'}, {'key': 'No of Cylinder', 'value': 3}, {'key': 'Values per Cylinder', 'value': 4}, {'key': 'Fuel Suppy System', 'value': 'GDi'}, {'key': 'Turbo Charger', 'value': 'Yes'}\]}, {'heading': 'Dimensions & Capacity', 'subHeading': 'Dimensions', 'list': \[{'key': 'Length', 'value': '3995mm'}, {'key': 'Width', 'value': '1790'}, {'key': 'Height', 'value': '1642'}, {'key': 'Wheel Base', 'value': '2500'}, {'key': 'Kerb Weight', 'value': '1465'}\]}, {'heading': 'Miscellaneous', 'subHeading': 'Miscellaneous', 'list': \[{'key': 'Gear Box', 'value': '7-Speed DCT'}, {'key': 'Drive Type', 'value': 'FWD'}, {'key': 'Seating Capacity', 'value': '5'}, {'key': 'Steering Type', 'value': 'Electric'}, {'key': 'Front Brake Type', 'value': 'Disc'}, {'key': 'Rear Brake Type', 'value': 'Drum'}, {'key': 'Tyre Type', 'value': 'Tubeless, Radial'}, {'key': 'Alloy Wheel Size', 'value': '16'}, {'key': 'No Door Numbers', 'value': '5'}, {'key': 'Cargo Volumn', 'value': '392'}\]}\], 'commonIcon': ''}

Same as above it is of 5 Layers.

### **5.car\_links:** 

Sample:https://www.cardekho.com/used-car-details/used-Kia-Sonet-Turbo-Dct-Anniversary-Edition-cars-Chennai\_9a50ab47-7b87-4649-951d-fadcf4f77ceb.htm

It is already Structured and it is not necessary for our modeling hence omitted.

The strategy adopted is similar to ‘ONION PEELING’ \- Layer by Layer Dictionaries will be converted as key value pairs where keys will be column names and values will be their row values.

## 2.Structuring the Data:

The First Outer Layer of Dictionaries are unwounded from all 4 columns and made into 4 dataframe.

***import pandas as pd***

***df \= pd.read\_excel("chennai\_cars.xlsx")***

***\#Initializing an empty list to hold structured data***  
***structured\_data \= \[\]***

***\# Looping through each row of the DataFrame***  
***for index, row in df.iterrows():***  
    ***row\_data \= {}***  
      
    ***\# Converting the string representation of the dictionary to an actual dictionary***  
    ***try:***  
        ***dict\_value \= eval(row\['new\_car\_detail'\])***    
        ***if isinstance(dict\_value, dict):***  
            ***row\_data \= dict\_value***  
    ***except Exception as e:***  
        ***print(f"Error parsing row {index}: {e}")***  
        ***row\_data \= None***

      
    ***structured\_data.append(row\_data)***

***\# Creating a DataFrame from the list of dictionaries in 'new\_car\_detail'***  
***unwound\_df \= pd.json\_normalize(structured\_data)***

***print(unwound\_df)***

***\#unwound\_df.to\_excel('unwound\_new\_car\_detail.xlsx', index=False)***

**eval(row\[col\])** : `eval()` is a Python function that evaluates a string containing a Python literal (such as a dictionary, list, tuple, numbers, strings, etc.) and converts it into its corresponding Python object***.*** 

Now we will Go Column by Column Unwounding the next Layers using the similar code and making it as a dataframe.Once 4 dataframes are obtained, all four of them are concatenated into a single table for the city.

***import pandas as pd***

***\# Concatenating the DataFrames column-wise***  
***combined\_df \= pd.concat(\[unwound\_df, unwound\_df1, unwound\_df2, unwound\_df3\], axis=1)***

***print(combined\_df)***

***\# Save the combined DataFrame to a new Excel file if needed***  
***\#combined\_df.to\_excel('combined\_data\_column\_wise.xlsx', index=False)***

Now The first Layer of Unstructuredness is removed. But even now some rows has list of nested dictionaries and a list of dictionaries.

Sample: ***top bottomData   heading  \\***  
***0     \[{'key': 'Registration Year', 'value': '2022',...       None  Features***     
And there is another issue: in the first extraction many similarly named dictionaries were converted into column names, hence they have to be renamed.

Index(\['it', 'ft', 'bt', 'km', 'transmission', 'ownerNo', 'owner', 'oem','model', 'modelYear', 'centralVariantId', 'variantName', 'price','priceActual', 'priceSaving', 'priceFixedText', 'trendingText.imgUrl', 'trendingText.heading', 'trendingText.desc', 'heading', 'top', 'bottomData', 'heading', 'top', 'data', 'commonIcon', 'heading', 'top', 'data', 'commonIcon'\], dtype='object')

***import pandas as pd***

***\#Getting the current column names***  
***original\_columns \= combined\_df.columns***

***\#Creating a new list to hold unique column names***  
***new\_columns \= \[\]***  
***column\_count \= {}***

***\# Looping through original columns and create unique names***  
***for col in original\_columns:***  
    ***if col in column\_count:***  
        ***column\_count\[col\] \+= 1***  
        ***new\_columns.append(f"{col}\_{column\_count\[col\]}")  \# Appending count as suffix***  
    ***else:***  
        ***column\_count\[col\] \= 1***  
        ***new\_columns.append(col)  \# Keeping original name for the first occurrence***

***\# Assigning the new column names to the DataFrame***  
***combined\_df.columns \= new\_columns***

***print(combined\_df.columns)***

Index(\['it', 'ft', 'bt', 'km', 'transmission', 'ownerNo', 'owner', 'oem', 'model', 'modelYear', 'centralVariantId', 'variantName', 'price', 'priceActual', 'priceSaving', 'priceFixedText', 'trendingText.imgUrl', 'trendingText.heading', 'trendingText.desc', 'heading', 'top', 'bottomData', 'heading\_2', 'top\_2', 'data', 'commonIcon', 'heading\_3', 'top\_3', 'data\_2', 'commonIcon\_2'\], dtype='object'). Hence Renamed.

Now, ***'top','top\_2', 'data','top\_3', 'data\_2'*** are the columns with a list of dictionaries which need to be unwound. Hence they are taken one by one, unwound and concatenated with the mother dataframe ie,. ***combined\_df***.

***import pandas as pd***

***\# Function to extract and convert 'top1' into a DataFrame***  
***def extract\_top\_to\_dataframe(main\_df):***  
    ***rows \= \[\]  \# To hold the extracted data***  
      
    ***\# Looping through each row in the main DataFrame***  
    ***for \_, row in main\_df.iterrows():***  
        ***top3\_data \= row\['top\_3'\]  \# Accessing the list directly***  
          
        ***\# Checking if the top1\_data is a list***  
        ***if isinstance(top3\_data, list):***  
            ***\# Creating a dictionary from the extracted key-value pairs***  
            ***row\_dict \= {item\['key'\]: item\['value'\] for item in top3\_data if 'key' in item and 'value' in item}***  
            ***rows.append(row\_dict)  \# Adding the dictionary to the rows list***  
        ***else:***  
            ***print(f"Unexpected format for row: {row}. Expected a list but got {type(top3\_data)}")***  
      
    ***\# Creating a new DataFrame from the rows list***  
    ***top3\_df \= pd.DataFrame(rows)***  
    ***return top3\_df***

***top3\_df \= extract\_top\_to\_dataframe(combined\_df)***

***print(top3\_df)***

Same Process is repeated for all the mentioned columns and all layers would be extracted. Then They are concatenated to form the final dataframe for the city.

***import pandas as pd***

***\# Concatenating the DataFrames column-wise***  
***final\_df\_chennai \= pd.concat(\[combined\_df, top\_df, top3\_df, data2\_df, top\_2\_df, data\_df\], axis=1)***

***print("Final DataFrame (final\_df\_chennai):")***  
***print(final\_df\_chennai)***

The Same Steps are repeated for all the 6 cities one by one and separated final dataframes to be made. And finally all 6 of them are concatenated to form our final unstructured dataset.

***import pandas as pd***

***\# Function to identify duplicate columns***  
***def find\_duplicate\_columns(df):***  
    ***return df.columns\[df.columns.duplicated()\].unique()***

***\# Checking for duplicate columns in each DataFrame***  
***duplicates\_chennai \= find\_duplicate\_columns(final\_df\_chennai)***  
***duplicates\_bangalore \= find\_duplicate\_columns(final\_df\_bangalore)***  
***duplicates\_delhi \= find\_duplicate\_columns(final\_df\_delhi)***  
***duplicates\_hyderabad \= find\_duplicate\_columns(final\_df\_hyderabad)***  
***duplicates\_jaipur \= find\_duplicate\_columns(final\_df\_jaipur)***  
***duplicates\_kolkata \= find\_duplicate\_columns(final\_df\_kolkata)***

***\# Printing duplicate columns for each DataFrame***  
***print("Duplicate columns in final\_df\_chennai:", duplicates\_chennai)***  
***print("Duplicate columns in final\_df\_bangalore:", duplicates\_bangalore)***  
***print("Duplicate columns in final\_df\_delhi:", duplicates\_delhi)***  
***print("Duplicate columns in final\_df\_hyderabad:", duplicates\_hyderabad)***  
***print("Duplicate columns in final\_df\_jaipur:", duplicates\_jaipur)***  
***print("Duplicate columns in final\_df\_kolkata:", duplicates\_kolkata)***

***\#Renaming duplicate columns in one of the DataFrames:***  
***def rename\_duplicate\_columns(df):***  
    ***cols \= pd.Series(df.columns)***  
    ***for dup in cols\[cols.duplicated()\].unique():***  
        ***cols\[cols\[cols \== dup\].index.values.tolist()\] \= \[dup \+ '\_' \+ str(i) if i \!= 0 else dup for i in range(sum(cols \== dup))\]***  
    ***df.columns \= cols***  
    ***return df***

***\# Renaming duplicate columns***  
***final\_df\_chennai \= rename\_duplicate\_columns(final\_df\_chennai)***  
***final\_df\_bangalore \= rename\_duplicate\_columns(final\_df\_bangalore)***  
***final\_df\_delhi \= rename\_duplicate\_columns(final\_df\_delhi)***  
***final\_df\_hyderabad \= rename\_duplicate\_columns(final\_df\_hyderabad)***  
***final\_df\_jaipur \= rename\_duplicate\_columns(final\_df\_jaipur)***  
***final\_df\_kolkata \= rename\_duplicate\_columns(final\_df\_kolkata)***

***columns\_hyderabad \= final\_df\_hyderabad.columns***

***\#Reindexing each DataFrame to have the same columns as Hyderabad, filling missing columns with NaN***  
***final\_df\_chennai\_reindexed \= final\_df\_chennai.reindex(columns=columns\_hyderabad)***  
***final\_df\_bangalore\_reindexed \= final\_df\_bangalore.reindex(columns=columns\_hyderabad)***  
***final\_df\_delhi\_reindexed \= final\_df\_delhi.reindex(columns=columns\_hyderabad)***  
***final\_df\_hyderabad\_reindexed \= final\_df\_hyderabad  \# Already has the full set of columns***  
***final\_df\_jaipur\_reindexed \= final\_df\_jaipur.reindex(columns=columns\_hyderabad)***  
***final\_df\_kolkata\_reindexed \= final\_df\_kolkata.reindex(columns=columns\_hyderabad)***

***\# Concatenating all DataFrames into a single DataFrame***  
***full\_data \= pd.concat(***  
    ***\[***  
        ***final\_df\_chennai\_reindexed,***  
        ***final\_df\_bangalore\_reindexed,***  
        ***final\_df\_delhi\_reindexed,***  
        ***final\_df\_hyderabad\_reindexed,***  
        ***final\_df\_jaipur\_reindexed,***  
        ***final\_df\_kolkata\_reindexed,***  
    ***\],***  
    ***ignore\_index=True,***  
***)***

***\# Verifying the shape of the full\_data DataFrame***  
***print(f'Shape of full\_data: {full\_data.shape}')  \# (8369, 200\)***

***‘Full\_data’*** \- FInal Structured Data is obtained.

## 3\. Cleaning the Data:

### 1.Irrelevant Column Removal:

There are a total of 200 Columns after making the dataset structured.   
**column names : it	ft	bt	km	transmission	ownerNo	owner	oem	model	modelYear	centralVariantId	variantName	price	priceActual	priceSaving	priceFixedText	Registration Year	Insurance Validity	Fuel Type	Seats	Kms Driven	RTO	Ownership	Engine Displacement	Transmission	Year of Manufacture	Mileage	Engine	Max Power	Torque	Wheel Size	Seats\_1	Color	Engine Type	Displacement	Max Power\_1	Max Torque	No of Cylinder	Values per Cylinder	Value Configuration	Fuel Suppy System	BoreX Stroke	Compression Ratio	Turbo Charger	Super Charger	Length	Width	Height	Wheel Base	Front Tread	Rear Tread	Kerb Weight	Gross Weight	Gear Box	Drive Type	Seating Capacity	Steering Type	Turning Radius	Front Brake Type	Rear Brake Type	Tyre Type	Alloy Wheel Size	No Door Numbers	Cargo Volumn	Top Speed	Acceleration	Ground Clearance Unladen	Power Steering	Power Windows Front	Air Conditioner	Heater	Adjustable Head Lights	Fog Lights Front	Anti Lock Braking System	Centeral Locking	Radio	Manually Adjustable Exterior Rear View Mirror	Child Safety Locks	Driver Air Bag	Power Adjustable Exterior Rear View Mirror	Brake Assist	Cd Player	Fog Lights Rear	Power Door Locks	Power Windows Rear	Electronic Multi Tripmeter	Leather Seats	Air Quality Control	Speakers Front	Cd Changer	Low Fuel Warning Light	Remote Trunk Opener	Tinted Glass	Halogen Headlamps	Usb Auxiliary Input	Passenger Side Rear View Mirror	Power Antenna	Day Night Rear View Mirror	Remote Fuel Lid Opener	Bluetooth	Fabric Upholstery	Glove Compartment	Anti Theft Alarm	Navigation System	Digital Odometer	Passenger Air Bag	Electric Folding Rear View Mirror	Dvd Player	Cassette Player	Audio System Remote Control	Number Of Speaker	Adjustable Steering	Tachometer	Wheel Covers	Accessory Power Outlet	Rear Seat Headrest	Integrated2Din Audio	Rear Seat Belts	Rear Folding Table	Driving Experience Control Eco	Engine Immobilizer	Leather Steering Wheel	Power Steering\_1	Power Windows Front\_1	Power Windows Rear\_1	Remote Trunk Opener\_1	Low Fuel Warning Light\_1	Accessory Power Outlet\_1	Vanity Mirror	Rear Seat Headrest\_1	Cup Holders Front	Seat Lumbar Support	Multifunction Steering Wheel	Cruise Control	Rear ACVents	Glove Box Cooling	Voice Control	Gear Shift Indicator	Lane Change Indicator	Adjustable Headrest	Remote Fuel Lid Opener\_1	Battery Saver	Trunk Light	Navigation System\_1	Engine Start Stop Button	Air Quality Control\_1	Rear Reading Lamp	Rear Seat Centre Arm Rest	Cup Holders Rear	Smart Access Card Entry	Height Adjustable Front Seat Belts	Steering Wheel Gearshift Paddles	Steering Mounted Tripmeter	Tailgate Ajar	Luggage Hook And Net	Power Boot	Hands Free Tailgate	Drive Modes	Find My Car Location	Remote Horn Light Control	Remote Engine Start Stop	Remote Climate Control	Real Time Vehicle Tracking	Active Noise Cancellation	Power Folding3rd Row Seat	Adjustable Head Lights\_1	Fog Lights Front\_1	Fog Lights Rear\_1	Power Adjustable Exterior Rear View Mirror\_1	Manually Adjustable Exterior Rear View Mirror\_1	Electric Folding Rear View Mirror\_1	Rain Sensing Wiper	Rear Window Wiper	Rear Window Washer	Rear Window Defogger	Alloy Wheels	Power Antenna\_1	Integrated Antenna	Tinted Glass\_1	Rear Spoiler	Removable Convertible Top	Roof Carrier	Sun Roof	Moon Roof	Side Stepper	Outside Rear View Mirror Turn Indicators**

The following Columns are with more than 95% null values and are directly removed.

**Noise Cancellation	Power Folding3rd Row Seat	Adjustable Head Lights\_1	Fog Lights Front\_1	Fog Lights Rear\_1	Power Adjustable Exterior Rear View Mirror\_1	Manually Adjustable Exterior Rear View Mirror\_1	Electric Folding Rear View Mirror\_1	Rain Sensing Wiper	Rear Window Wiper	Rear Window Washer	Rear Window Defogger	Alloy Wheels	Power Antenna\_1	Integrated Antenna	Tinted Glass\_1	Rear Spoiler	Removable Convertible Top	Roof Carrier	Sun Roof	Moon Roof	Side Stepper	Outside Rear View Mirror Turn Indicators Passenger Air Bag	Electric Folding Rear View Mirror	Dvd Player	Cassette Player	Audio System Remote Control	Number Of Speaker	Adjustable Steering	Tachometer	Wheel Covers	Accessory Power Outlet	Rear Seat Headrest	Integrated2Din Audio	Rear Seat Belts	Rear Folding Table	Driving Experience Control Eco	Engine Immobilizer	Leather Steering Wheel Fog Lights Rear	Power Door Locks	Power Windows Rear	Electronic Multi Tripmeter	Leather Seats	Air Quality Control	Speakers Front	Cd Changer	Low Fuel Warning Light	Remote Trunk Opener	Tinted Glass	Halogen Headlamps	Usb Auxiliary Input	Passenger Side Rear View Mirror	Power Antenna	Day Night Rear View Mirror	Remote Fuel Lid Opener	Bluetooth	Fabric Upholstery	Glove Compartment	Anti Theft Alarm priceSaving	priceFixedText**

The following columns are irrelevant to price prediction and hence they are directly removed:

**Wheel Size Length	Width	Height	Wheel Base	Front Tread	Rear Tread	Kerb Weight	Gross Weight Turning Radius Cargo Volumn Acceleration Ground Clearance Unladen Digital Odometer	Power Steering\_1	Power Windows Front\_1	Power Windows Rear\_1	Remote Trunk Opener\_1	Low Fuel Warning Light\_1	Accessory Power Outlet\_1	Vanity Mirror	Rear Seat Headrest\_1	Cup Holders Front	Seat Lumbar Support	Multifunction Steering Wheel	Cruise Control	Rear ACVents	Glove Box Cooling	Voice Control	Gear Shift Indicator	Lane Change Indicator	Adjustable Headrest	Remote Fuel Lid Opener\_1	Battery Saver	Trunk Light	Navigation System\_1	Engine Start Stop Button	Air Quality Control\_1	Rear Reading Lamp	Rear Seat Centre Arm Rest	Cup Holders Rear	Smart Access Card Entry	Height Adjustable Front Seat Belts	Steering Wheel Gearshift Paddles	Steering Mounted Tripmeter	Tailgate Ajar	Luggage Hook And Net	Power Boot	Hands Free Tailgate	Drive Modes	Find My Car Location	Remote Horn Light Control	Remote Engine Start Stop	Remote Climate Control	Real Time Vehicle Tracking Centeral Locking	Radio	Manually Adjustable Exterior Rear View Mirror	Child Safety Locks	Driver Air Bag	Power Adjustable Exterior Rear View Mirror	Brake Assist	Cd Player	Navigation System Centeral Locking	Radio	Manually Adjustable Exterior Rear View Mirror	Child Safety Locks	Driver Air Bag	Power Adjustable Exterior Rear View Mirror	Brake Assist	Cd Player	Navigation SystemCenteral Locking	Radio	Manually Adjustable Exterior Rear View Mirror	Child Safety Locks	Driver Air Bag	Power Adjustable Exterior Rear View Mirror	Brake Assist	Cd Player	Navigation System BoreX Stroke	Compression Ratio No of Cylinder	Values per Cylinder	Value Configuration	Fuel Suppy System	Turbo Charger	Super Charger Heater	Adjustable Head Lights	Fog Lights Front**

The repetitive columns are removed:  
**There are two Transmission columns (Automatic\\Manual), two Year of Manufacture Columns , three Seats Columns,two Fuel Type Columns,three Owners Type Columns, three Engine Displacement Columns, two Torque Type Columns ,and two Power Type Columns**.

Now the shape of the dataframe is reduced to: 8369 rows × 33 columns

### 2.Null Value Removal:

- If similar columns are available with matching values, those are filled.  
- If number of null values are less and matching values not available they are dropped  
- Column with more than 50% null values are removed 

By applying all these methods all null values are removed. We are down to 22 columns.

### 3.Pre-Processing:

- Bt: Datatype is checked and it is categorical.  
- Km: unwanted strings are removed and converted to integer  
- Transmission: Datatype is checked and it is categorical.  
- OEM:  Datatype is checked and it is categorical.  
- Model:  Datatype is checked and it is categorical.  
- Price: Unwanted strings are removed and changed to integer.  
- Insurance validity: Datatype is checked and it is categorical. Duplicate value merged.  
- Manufacture Year: Kept as integer itself for further processing  
- Registration year:Kept as integer itself for further processing  
- Fuel Type: Datatype is checked and it is categorical.  
- RTO:Datatype is checked and it is categorical.unwanted strings are removed, repetitive and spelling mistakes are corrected for similarity.Duplicates are merged.  
- State: A new column is created for further use from the RTO column by mapping.  
- Owner number: Kept as integer itself  
- Displacement: Kept as float type  
- Mileage: Unwanted strings removed and kept as floats.  
- Max power:Unwanted strings removed and kept as floats.  
- Torque:Unwanted strings removed and kept as floats.  
- Seats: Kepts as integer  
- Colors:  Datatype is checked and it is categorical.  
- Door No: Kept as integer  
  


All Data cleaned and brought to necessary data types, unwanted strings are removed, duplicates are deleted, null values are removed.

