# -*- coding: utf-8 -*-
# Copyright 2016 Siddharth Bhalgami <siddharth.bhalgami@techreceptives.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Web Widget - Image WebCam",
    "summary": "Allows to take image with WebCam",
    "version": "12.0.1.0.0",
    "category": "web",
    "website": "https://www.techreceptives.com",
    "author": "Tech Receptives, "
              "Odoo Community Association (OCA), "
              "Kaushal Prajapati，"
              "山西清水欧度信息技术有限公司，"
              "John Lin",
    "license": "LGPL-3",
    "data": [
        "views/assets.xml",
    ],
    "depends": [
        "web",
    ],
    "qweb": [
        "static/src/xml/web_widget_image_webcam.xml",
    ],
    "installable": True,
}
