import os
from iptcinfo3 import IPTCInfo
from flask import Flask, request, render_template, send_from_directory, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/', methods=['GET'])
def get_gallery():
    imgList = os.listdir('./images')

    tags = []
    description = []
    title = []

    for imgName in imgList:
        img_path = "images/"+imgName

        imgIPTC_info = IPTCInfo(img_path, force="True")

        imgIptcKeywordDecoded = []
        for keywords in imgIPTC_info['keywords']:
            imgIptcKeywordDecoded.append(keywords.decode('utf-8'))
        tags.append(imgIptcKeywordDecoded)

        imgIptcDescrpitionDecoded = []
        if (imgIPTC_info['caption/abstract'] == None):
            imgIptcDescrpitionDecoded.append("Description not present")
        else:
            imgIptcDescrpitionDecoded.append(
                imgIPTC_info['caption/abstract'].decode('utf-8'))
        description.append(imgIptcDescrpitionDecoded)

        imgIptcTitleDecoded = []
        if (imgIPTC_info['object Name'] == None):
            imgIptcTitleDecoded.append("Title not Present")
        else:
            imgIptcTitleDecoded.append(
                imgIPTC_info['object Name'].decode('utf-8'))
        title.append(imgIptcTitleDecoded)

    return render_template("index.html", image_names=imgList, description=description, tags=tags, title=title)

# --------------------------------------------------------------------------------------------------------


def Query(imgList, queried_tag):
    resultImages = []
    for imgName in imgList:
        img_path = "images/"+imgName

        imgIPTC_info = IPTCInfo(img_path, force="True")

        if (queried_tag.encode('utf-8') in imgIPTC_info['keywords']):
            resultImages.append(imgName)
    return resultImages


@app.route('/', methods=['POST'])
def get_data():
    imgList = os.listdir('./images')

    if request.form.get('queryByTag'):

        queried_tag = request.form['queryByTag']
        resultImages = Query(imgList, queried_tag)

        return render_template("result.html", resultImages=resultImages)

    else:
        for imgName in imgList:

            if (request.form.get(imgName)):

                img_path = "images/"+imgName

                imgIPTC_info = IPTCInfo(img_path, force="True")

                if request.form.get("submit_btn") == "update":
                    new_description = request.form.get(imgName)
                    imgIPTC_info['caption/abstract'] = new_description.encode(
                        'utf-8')

                elif request.form.get("submit_btn") == "title":
                    new_title = request.form.get(imgName)
                    imgIPTC_info['object Name'] = new_title.encode('utf-8')

                elif request.form.get("submit_btn") == "add":
                    new_tag = request.form.get(imgName)
                    imgIPTC_info['keywords'].append(new_tag.encode('utf-8'))

                elif request.form.get("submit_btn") == "remove":
                    remove_tag = request.form.get(imgName)
                    imgIPTC_info['keywords'].remove(remove_tag.encode('utf-8'))

                imgIPTC_info.save()

        return redirect(url_for("get_gallery"))


if __name__ == "__main__":
    app.run(debug=True)
