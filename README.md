# FamPay Backend Assignment

## 1. Getting the project files
      1. create a folder with any name e.g 'fp'.
      2. open the folder with git bash.
      3. clone the project : `git clone https://github.com/jkjarvis/famPay `

<!-- ## 2. Setting the project
      1. Start docker engine.
      2. Go to fp and then : `cd famPay`
      3. Run : `docker-compose -f docker-compose.yml up -d` -->

## 3. Creating virtual environment and install dependencies
      1. Check for python version : python -V (should be 3.7 or above).
      2. In fp , do : `cd famPay` , the location where docker-compose.yml file exists.
      3. run : `pip install virtualenv`
      4. run : `python -m virtualenv env`
<!--       5. FOR WINDOWS : run `env\Scripts\activate `
         For MAC/LINUX : run `source env/bin/activate` -->
<!--       6. After the virtualenv is activate , run : `pip install -r ../requirements.txt ` (FOR MAC/LINUX) OR `pip install -r ..\requirements.txt ` (FOR WINDOWS)
      7.Wait for the dependencies to download. -->

## 4. Running the project
      1. Run : `docker-compose build`
      2. Run : `docker-compose -f docker-compose.yml up -d`
      
<!--       1. Make sure you are in `fp/fampay/famPay` directory.
      2. Run : `python manage.py runserver`
      3. Open 'http://127.0.0.1:8000' in chrome or firefox.
      4. You should see the default rest api homepage. -->

## 5. Listing the stored videos
      1. While the server is running, go to `http://127.0.0.1/video' in chrome or firefox
      2. This should list all the videos stored till now. Keep refreshing after few seconds and see if the results get refreshed (depends upon if a new video is uploaded to 'cricket' query).

## 6. Searching a video with a keyword
      1. While the server is running, go to `http://127.0.0.1/search'.
      2. There is a button with name 'filters' , click on it.
      3. A search box will appear, enter the keyword you want to search and press search button.
      OR
      1. While the server is running, go to `http://127.0.0.1/search' and change it to `http://127.0.0.1/search?search=keyword` where keyword is the word you want to search.
      2. To search multiple words, keyword = 'word1+word2' e.g keyword = 'how+tea'.
      
