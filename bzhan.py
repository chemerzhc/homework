from string import Template

s = Template('https://www.toutiao.com/article/v4/tab_comments/?aid=24&app_name=toutiao_web&offset=${page}&count=20&group_id=7367699784716796451&item_id=7367699784716796451&_signature=_02B4Z6wo00f01OdOBRAAAIDA0GrBTjUEv-znagGAAF-7DbOQ5d5qqjbPphpqUEsEO1ZcYPxyUnx-K6L6V0A35sGLfXf-dLeiSghSL6HhYUu0PlY093eLLEBC8jd1gNp8MbsCxPePvd0NBaCAaa')
page = 1
url = s.substitute(page=page)
print(url)