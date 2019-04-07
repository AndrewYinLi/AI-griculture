![AI-griculture](https://raw.githubusercontent.com/AndrewYinLi/AI-griculture/master/static/resources/banner2.png)

## Inspiration:

In order to feed today's global population, we currently need farmland equivalent to the size of South America. Despite the exorbitant amount of land already allocated to agriculture, an estimated 815 million people worldwide still go to bed hungry each night. Moreover, the worldwide population is estimated to be **9 billion by the end of 2050**. Modern-day cities in the world already contain half of the world's population, which follows that the impact of the projected surge in global population will drastically decrease the amount of habitable land to extreme levels in order to maintain modern infrastructure. **In this rapidly changing world already brimming with hunger and agricultural difficulties caused by lack of land, we believe that our solution with underpinnings in sustainable agriculture and artificial intelligence provides a feasible solution**.

## What it does

AI-griculture automates the fundamental aspects of cultivation and provides intuitive feedback to a dashboard that displays metrics on moisture levels. Our hack utilizes a random decision forest model that uses the data that we collect from moisture sensors to determine when and how much to water our plant. Moreover, artificial lighting is activated to ensure that our plant receives enough light during certain hours of the day imperative to photosynthesis and healthy growth.

![Short-term moisture](https://raw.githubusercontent.com/AndrewYinLi/AI-griculture/master/static/resources/moistureshort.png)

![Long-term moisture](https://raw.githubusercontent.com/AndrewYinLi/AI-griculture/master/static/resources/moisturelong.png)

## How we built it

![AI-griculture Technolgies](https://raw.githubusercontent.com/AndrewYinLi/AI-griculture/master/static/resources/tech.png)

We employed a random decision forest model from scikit-learn and hosted on Google Cloud platform to determine whether the plant needed water. Parameters such as temperature, moisture, humidity, availability of light and weather were used to facilitate prediction in our model. We also considered certain factors such as the principle of a plant requiring at least 16 hours of light per day to stimulate photosynthesis and a threshold water supply to guide our model's decisions. Analytics are provided on our interactive user interface built using React. The Javascript frontend interacts with a Python Flask backend. Our hardware setup consists of an Adafruit Crickit controlling a motor that enables water to flow through our watering tube on command, as well as light and moisture sensors.

## Challenges we ran into

In the beginning of the hackathon, we wrote down tons of ideas on a Google Document. However, the idealization phase took too much time to find the right problem to work on. We thought about every single SDGs and finally pick a problem that connects with a large user group and has a large scope of improvement. 

Our web platform gives a real time data from various sensors and helps us to visualize every detail of the farm in a very precise and clear manner. We used Google Cloud Platform to host our Scikit Learn model and get real time predictions on the optimal actions to be taken. Dealing with real time data prediction was the key challenge that we faced. Data state management was difficult considering it took time to communicate efficiently. We first met each other during the hackathon :)

## Accomplishments that we're proud of

We have an automated farming system measures many aspects of a plant using sensors, such as moisture, water and temperature metrics that uses machine learning to facilitate management decisions. This robot can be manipulated by a beautiful dashboard made completely from scratch. Moreover, we are proud to have leveraged Google Cloud Platform to host our scikit-learn random decision forest and for prediction.

## What's next for AI-griculture

Our vision is to incorporate technologies such as hydroponics to make a completely automated artificial environment for plant growth. Scraping real-time weather data to better facilitate decisions is also the next step. We plan to start a venture by designing our prototype into an end product and by scaling it in the cities like San Francisco. Also our machine learning model should be improvised to incorporate more labels to predict more efficient data. One challenge that we want to solve is the electricity problem by using renewable sources like Solar Panels. 
