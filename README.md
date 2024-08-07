# Project Go Carbon Neutral

This project focusses on building carbon emission calculator using BVG API, the user can make sustainable choices, track carbon footprint. In Germany 7.26 metric tons of Co2 emission as of 2020. And, BVG being the top transporation company in Berlin,Germany, the company has been moving towards making sustainable choices everyday. At the rapid rate of environmental hazards and climate change, it is a responsibility of each individual to make better choices for your well being as well as our planets. In this project, I'm going to show you exactly how you can make changes in your everyday life to bring this difference. 

Whenever I speak about creating change on social issues, I have been usually asked, How is 1 person's change making a difference to the social issue? while a single person’s change might seem small, the combined effect of many individuals making conscious choices can drive substantial progress. My project with the BVG API is a perfect example of how technology can empower people to make informed, sustainable choices, ultimately contributing to a healthier planet.

# Project Roadmap 

While working on this project, I saw potential in creating a large scale project, however every project start with small simple actionable steps, so in the first phase of the project,  I am going to explore on the data points, determine the emission estimates for each mode of transportaion, build a carbon footprint calculator. 

# Data 

As discussed earlier, the data is collected using BVG API, while BVG do not reveal information about carbon emission, we have data related to the transportation route in real-time, after reading tons of BVG reports across years as of 2024, the carbon factors for model of transportation is the following: 'Suburban': 100,'Subway': 70,  'Tram': 50,'Bus': 120,'Ferry': 150,'Express': 90,'Regional': 110. While this information is a starting point, How do we determine carbon emission of the user?

# Calculate emission 

Now that we have determined the starting point of data points and have a clear view of the end goal, we need to create a problem statement that can be acieved based on our findings. 

For example, 
Our user Alexander is using Go Carbon Neutral platform, I need some information from Alexander so that I can use user's trip data. In our case, Origin and destination. For example: Alexander is travelling from Berlin Zoo to East Side Gallery.

Alexander is a eco-conscious traveler and wellness-oriented individual. #BeLikeAlexander. 

I will let you in on a little secret - A few background information on how we use this data to help Alexander make sustainable choice. 

For each trip or segment of the trip, I will need to:

1. Retrieve the transportation modes from the BVG API.
2. Retrieve or estimate the distance traveled for that segment.
3. Using the carbon factors provided, we can calculate Carbon emission:

- Emission = Distance × Carbon Factor

If Alexander travlled 9 km from Berlin Zoo to East Side Gallery by bus:
* Carbon Factor for Bus: 120 grams CO2 per km.
     Emission = 10 km × 120 g CO2/km = 1200 g CO2

As simple as it sounds, I need to do not have distance data, will I be able determine the distance based on Alexander's input? 

It is possible using Google Maps API, Send a request to the API with the addresses of Berlin Zoo and East Side Gallery to get the distance.

Now we can determine, Carbon Emission for all routes from Berlin Zoo to East Side Gallery for Alexander, Now alexander can make sustainable choice. (Yayy!)


