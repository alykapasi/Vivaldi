# Spotify Applet

***Spotify have changed their API - need to edit code and modify the implementation maybe***

## Spotify End-to-End Data Engineering and Analysis Project

Aly Kapasi | aly.kapasi@icloud.com | /in/alykapasi

### Motivation

I am a lover of music. I listen to music, while I do almost anything. While studying: I listen to music, while bathing: I listen to music, while: eating I listen to music even while sleeping: I listen to music. One of the best feelings I get is when I find 'under-the-radar' music (basically music that isnt mainstream YET) I'm sure that's the thrill A&R representatives used to get when they discovered the next big band. 

A big source of frustration I have with a lot of streaming services and one of the reasons I switched from Spotify Freemium -> Apple Music -> Pandora -> SoundCloud -> Spotify Premium was because I was very underwhelmed by the suggestions. I feel that suggestions were the crux of a streaming service's business model, much like Netflix. I felt that Spotify's competitive advantage over behemoths like Apple and Pandora was their suggestions, but as I have used Spotify over the years, I have found less and less songs I liked from the suggested section, though that could also be because I have such a varied taste in music that it is a difficult task to quantify my preferences.

Towards the tailend of the year, Spotify releases a small 'story', which describes the user's music tastes over the year. Being data inclined, analytically minded and aspiring data scientist myself, I loved to see my listening data visualized and made digestable. This not only gave an insight into how spotify catalogued and classified my music profile, but it also gave me an insight into how my music changes have evolved over the years.

This project is also to showcase my data science and engineering skills, as it will demonstrate my ability to create and maintain ETL/ELT pipelines, dashboards and deploy different types of Machine Learning / Artificial Intelligence Technologies.

### Design and Implementation

The Design Process was split into a couple of steps:

(1) EXTRACT => Get the data from spotify using their API and the python requests library.

(2) LOAD => Transfer the data into an SQLite3 Database (only one I know how to use : may need to reconsider if scaling is needed)

(3) TRANSFORM => Apply the necessary transformations to the data that are needed to be usable for machine learning and visualization (dashboards)

(4) Create DAG using Airflow/Luigi/AWS Step... to automatically run the pipeline and update the table after 50 plays. **Need to think of a clever way to do so as there is no way of alerting the script when x amount of songs have played.**

(5) Use the data to create data visualizations and apply various ML models to help identify similar songs. **Problem here is where to first get a list of all songs on spotify, second compute effieciently as there will be a massive amount of songs, some may be nearly identical**

### Possible Extensions

(1) Implement a feedback system to help the algorithm fine tune predictions

(2) Allow for clustering on audio samples; would require an API to be built
    • this would ideally be the main point of reference for a recommender  system as this is instead of clustering by tags and profiles, they would be clustered by actual audio characteristics.

(3) Grow to allow all types of users not only spotify but: apple music, pandora, soundcloud, deezer, tidal, etc.

(4) **dream implementation** virtual DJ that mixes tracks better and also remixes songs on the fly

### Current Expectations

(31/03) I don't really have many expectations in terms of performance or quality at this point, as I have very little experience in the other aspects of this project such as building a UI or working with audio data. I also am not very confident in the ML models being able to predict with any great accuracy or to provide any significant insight, as if it was that easy im sure one of the large streaming services would've already implemented it.

Nonetheless, I feel that if I can create something worthwhile it may help people find music better and perhaps de-mystify their suggested section.
