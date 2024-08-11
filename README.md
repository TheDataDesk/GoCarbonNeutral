# 🌍 Project Go Carbon Neutral 🚶‍♂️

Welcome to **Project Go Carbon Neutral**, where technology meets sustainability! This project is all about empowering you to make eco-friendly choices by tracking your carbon footprint using the BVG API. Whether you're commuting through Berlin's bustling streets or exploring its iconic landmarks, this project will guide you in reducing your carbon emissions and contributing to a greener planet. 🌱

## 🚀 Why This Project?

In 2020, Germany emitted a staggering 7.26 metric tons of CO2 per capita. BVG, Berlin's leading transportation company, is committed to reducing its environmental impact. But the responsibility doesn't just lie with large organizations—it’s up to each of us to make better choices for our well-being and the health of our planet. 🌎

Whenever I talk about social change, people often ask, *"How can one person's actions make a difference?"* The answer is simple: while a single person's efforts might seem small, the collective impact of many individuals making sustainable choices can drive significant progress. This project is a shining example of how technology can help you make informed, sustainable decisions every day.

## 🛤️ Project Roadmap

Building a carbon emission calculator isn't just a cool tech challenge—it's a journey toward sustainability. Here's how we'll get there:

1. **Explore Data Points**: Dive deep into the data provided by the BVG API. We'll estimate emissions for different modes of transportation.
2. **Carbon Footprint Calculator**: Build a tool that helps you calculate your carbon emissions based on your travel choices.
3. **Sustainable Choices**: Provide actionable insights and recommendations for reducing your carbon footprint.

### 🔍 Data Breakdown

Our data comes from the BVG API. While BVG doesn't directly share carbon emissions data, we do have access to real-time transportation routes. After analyzing numerous BVG reports (as of 2024), we've determined the following carbon factors for various modes of transportation:

- **Suburban**: 100 g CO2/km
- **Subway**: 70 g CO2/km
- **Tram**: 50 g CO2/km
- **Bus**: 120 g CO2/km
- **Ferry**: 150 g CO2/km
- **Express**: 90 g CO2/km
- **Regional**: 110 g CO2/km

With this data, we can start calculating the carbon emissions for each trip. 🎯

## 🧮 Calculate Your Emissions

Let’s bring this data to life with an example! Meet Alexander, an eco-conscious traveler and wellness-oriented individual. #BeLikeAlexander

Alexander is using the **Go Carbon Neutral** platform to plan his trip from Berlin Zoo to East Side Gallery. Here's how we'll help Alexander make a sustainable choice:

1. **Input the Journey**: Alexander provides his origin and destination.
2. **Retrieve Transportation Modes**: We fetch the transportation modes via the BVG API.
3. **Estimate Distance**: If the distance isn't readily available, we'll use the Google Maps API to calculate it.
4. **Calculate Emission**: 

   Emission = Distance \ Carbon Factor 

   - For example, if Alexander travels 9 km by bus:

Emission = 9 km \ 120 g CO2/km = 1080  g CO2


Now, Alexander can see the carbon emissions for different routes and choose the most eco-friendly option. 🎉

## 🌟 Be Like Alexander

Alexander chose the route with the lowest carbon emissions, contributing to a healthier planet. By using this tool, you can do the same—small choices, big impact. Remember, each step toward sustainability is a step toward a better future. Let's make it count!

---

Happy travels, and thank you for making a difference! If you have any questions or want to contribute, feel free to reach out. Together, we can #GoCarbonNeutral! 🌍💚

