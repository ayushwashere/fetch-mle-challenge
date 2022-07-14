# Fetch MLE Takehome Challenge: Image Pixels

Challenge Description: https://fetch-hiring.s3.amazonaws.com/machine-learning-engineer/image-coordinates.html

## Introduction
Given a rectangle (sides parallel to x and y-axis), we want to create an image with m * n (m = rows, n = cols ) equally spaced pixels.
The user calls the web service at the end point `/image-pixels` with the dimensions (m, n) as well as the corners of the rectangle

## Usage
Unable to create Docker container due to some dependency issues with numpy version. I will continue trying to fix this issue. In the mean time, the web service can be run perfectly by downloading this git folder and running the following commands:


```
pip3 -r install requirements.txt
export FLASK_APP=routes
flask run
```

In another terminal window, use the following to test the web service:

```
curl -H "Content-Type: application/json" -X POST -d '{"dimensions": [2,4], "corner_points": [[1.5,8], [4,8], [1.5,1.5], [4,1.5]]}' http://127.0.0.1:5000/image-pixels
```


## Output
```
{
    'solution' : [
        [[1.0, 3.0], [2.0, 3.0], [3.0, 3.0]],
        [[1.0, 2.0], [2.0, 2.0], [3.0, 2.0]],
        [[1.0, 1.0], [2.0, 1.0], [3.0, 1.0]]
    ]
}
```

Note: The output is a multi-dimensional array and not a numpy.ndarray.

## Design Details
1. There are 2 routes. `/` exists only for providing some basic information and `/image-pixels` takes a `POST` request with a JSON object strucutured as mentioned above.
2. Since the corner point coordinates can be provided in any order, the code determines which one is on the left_top, left_bottom, right_top, right_bottom using a simple logic - The top left coordinate will be the one where the x-coordinate of the rectangle will be the min and the y-coordiante of the rectangle will be the max. Similarly, the left bottom corner will have minimum of both the x and y coordinates and the right top corner will have the maximum of the x and y coordinates. Lastly, the right bottom corner will have the minimum of y-coordinates and the maximum of the x-coordinates. This logic is consistent throughout the cartesian coordinate plane, regarless of whether the rectangle is in the first, second, third or fouth quadrant and even convering more than one quadrants.
3. In order to generate the pixels, I used the `numpy.linspace` fucntions. Thus function allows us to define the start, end and the number of evenly-spaced elements. In order to create a 2D grid of pixel, I first create X & Y coordinates between the left_top and right_top corners. Then I create X & Y coordinates between the left_bottom and right_bottom corners and then create subsequent pixels along the respecive columns connecting the top and bottom layer.