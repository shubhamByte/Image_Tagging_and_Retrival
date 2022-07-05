import os
from iptcinfo3 import IPTCInfo
from flask import Flask, request, render_template, send_from_directory, jsonify, redirect, url_for

app = Flask(__name__)

# function to read images from the directory
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

def extractAndUpdate():
    
    # making list of names of the images in the directory
    imgList = os.listdir('./images')

    # these three lists will be send to the html document. It will contain information of each image.
    tags = []                   # list of lists
    description = []            # list of strings
    title = []                  # list of strings

    # looping through each image in the list and updating the above three lists according to it
    for imgName in imgList:

        # creating path
        img_path = "images/"+imgName

        # getting the iptc data of the image using module
        imgIPTC_info = IPTCInfo(img_path, force="True")


        # we are first geting the keyword list using our module then decoding it using utf-8 then appending it to the main tags list.  

        # Tags
        imgIptcKeywordDecoded = []
        for keywords in imgIPTC_info['keywords']:
            imgIptcKeywordDecoded.append(keywords.decode('utf-8'))
        tags.append(imgIptcKeywordDecoded)

        # Description
        imgIptcDescrpitionDecoded = []
        if (imgIPTC_info['caption/abstract'] == None):   # using if else to check when no description is present.
            imgIptcDescrpitionDecoded.append("Description not present")
        else:
            imgIptcDescrpitionDecoded.append(
                imgIPTC_info['caption/abstract'].decode('utf-8'))
        description.append(imgIptcDescrpitionDecoded)

        # Title
        imgIptcTitleDecoded = []
        if (imgIPTC_info['object Name'] == None):       # using if else to check when no title is present.
            imgIptcTitleDecoded.append("Title not Present")
        else:
            imgIptcTitleDecoded.append(
                imgIPTC_info['object Name'].decode('utf-8'))
        title.append(imgIptcTitleDecoded)


    return title,description,tags


# function to render the main page. it gets iptc data but not change any of it.
@app.route('/', methods=['GET'])
def get_gallery():
    
    
    # making list of names of the images in the directory
    imgList = os.listdir('./images')

    title,description,tags = extractAndUpdate()

    # rendering the html by passing the index.html and the above mentioned list
    return render_template("index.html", image_names=imgList, description=description, tags=tags, title=title)

# --------------------------------------------------------------------------------------------------------

# function to get data from  the index.html and change the iptc data of the images accordingly
@app.route('/', methods=['POST'])
def get_data():

    # list of images in the directory
    imgList = os.listdir('./images')

    if request.form.get('queryByTag'):                  # checks if queryByTag(name) form is submitted.(means query is runned.)

        queried_tag = request.form['queryByTag']        # get the data from form
        resultImages = Query(imgList, queried_tag)      # calls the query function which returns the list of matching images
        titleResult = []
        descriptionResult = []
        tagsResult = []
        title,description,tags=extractAndUpdate()
        for resultImg in resultImages:
            titleResult.append(title[imgList.index(resultImg)])
            descriptionResult.append(description[imgList.index(resultImg)])
            tagsResult.append(tags[imgList.index(resultImg)])
        return render_template("result.html", resultImages=resultImages,titleResult=titleResult,descriptionResult=descriptionResult,tagsResult=tagsResult)

    else:
        # if the query form is not submitted, then we will loop through all the images and check which image's form is submitted using name attribute of the form. name attribute of the form is containing imgName.
        for imgName in imgList:

            if (request.form.get(imgName)):     # checks form of which particular image's form is submitted

                img_path = "images/"+imgName
                print(request.form.get(imgName))
                imgIPTC_info = IPTCInfo(img_path, force="True")

                # now we are checking which form of the given image is filled. we are using 'value' attribute of the button.

                # description form 
                if request.form.get("submit_btn") == "update":
                    new_description = request.form.get(imgName)
                    imgIPTC_info['caption/abstract'] = new_description.encode(
                        'utf-8')

                # title form
                elif request.form.get("submit_btn") == "title":
                    print("yes")
                    new_title = request.form.get(imgName)
                    imgIPTC_info['object Name'] = new_title.encode('utf-8')

                # tag-add form
                elif request.form.get("submit_btn") == "add":
                    new_tag = request.form.get(imgName)
                    imgIPTC_info['keywords'].append(new_tag.encode('utf-8'))

                # tag-remove form
                elif request.form.get("submit_btn") == "remove":
                    remove_tag = request.form.get(imgName)
                    imgIPTC_info['keywords'].remove(remove_tag.encode('utf-8'))

                # after changing the IPTC, saving the image.
                imgIPTC_info.save()

        # redirecting to get gallery function which in turn will render index.html with updated IPTC info.
        return redirect(url_for("get_gallery"))

# ===========================================================================

# function to matck the values/text in the image's IPTC data
# returns list of matched images
def Query(imgList, queried_tag):
    resultImages = []
    for imgName in imgList:
        img_path = "images/"+imgName

        imgIPTC_info = IPTCInfo(img_path, force="True")

        if (queried_tag.encode('utf-8') in imgIPTC_info['keywords']):
            resultImages.append(imgName)
    return resultImages

if __name__ == "__main__":
    app.run(debug=True)
