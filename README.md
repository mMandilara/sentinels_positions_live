# sentinels_positions_live
This project creates an html file running on your local http://127.0.0.1:5000, which shows the live locations of ESA's twin satellites Sentinel-2A and 2B.
![sentinels](https://github.com/mMandilara/sentinels_positions_live/assets/107554706/1e92d060-25db-448d-83b8-f8bdf610d507)

Using python the fetcher.py fetches every 10 seconds the data for longtitude and latitude from [N2YO.com](https://www.n2yo.com/), for both S2A and S2B satellites. With the site.py a plot is created to visualize their positions, using the [plotly](https://plotly.com) library. Then, an html is created to show this plot along with a few info written about the satellites, that I have added in the index.html.

### ***Feautres of plotly***

By hovering your mouse over the map you can see the coordinates corresponding to the long and lat lines on the map and if you hover over the red and blue points (the satellites) you can see some info about their location. 

![image](https://github.com/mMandilara/sentinels_positions_live/assets/107554706/85b95916-4b28-44bb-9792-b45a900a3bd5)

If you want to hide one of the satellites, just click on its name on the right side of the map and it will disappear from the map. And to reappear click on the name again.

## Note 1:

To see the site and the map site.py needs to run first.

Also, do not forget, to get updated data of the satellites fetcher.py needs to be running on the background. If it isn't, the html will show the last data that were saved on json files.

## Note 2:

There is also the libraries that are used in the environment. To create a conda env from this only need to run:
```
conda env create -f environment.yml
```
