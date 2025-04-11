"""
Function:
Module feature: Camera preview, camera decoder, and camera capture.
Currently supported modules: EC600N Series, EC800N Series, EC600M Series, EC800M Series, EC600U-CN and EC200U-CN.
Note: If the preview feature is needed, please initialize the LCD object first by referring to the content of lcd class in the machine module before initializing the camera object.


Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/medialib/camera.html
"""


class CamPreview(object):
    """Camera Preview

    Class feature: Camera previewing.
    Note: Please initialize the LCD before using this feature.
    Descriptions: https://python.quectel.com/doc/API_reference/en/medialib/camera.CamPreview.html
    """

    def __init__(self, model, cam_w, cam_h, lcd_w, lcd_h, perview_level):
        """Creates a camPreview object.

        :param model: Integer type. Camera model. Click here for corresponding camera model.
        :param cam_w: Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
        :param cam_h: Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
        :param lcd_w: Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
        :param lcd_h: Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.
        :param perview_level: Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
        Corresponding Camera Model:
        Number	Camera Model	Communication Method
        0	GC032A	SPI
        1	BF3901	SPI
        """

    def open(self):
        """This method enables the camera preview feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def close(self):
        """This method disables the camera preview feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """


class CamDecoder(object):
    """Camera code scanning.

    Note: Please initialize the LCD before enabling preview feature.
    Descriptions: https://python.quectel.com/doc/API_reference/en/medialib/camera.CamDecoder.html
    """

    def __init__(self, model, decode_level, cam_w, cam_h, perview_level, lcd_w, lcd_h):
        """Creates a camScandecode object.

        :param model: Integer type. Camera model. It can be set to 0 or 1. Click here for corresponding camera model.
        :param decode_level: Integer type. Decoding level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
        :param cam_w: Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
        :param cam_h: Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
        :param perview_level: Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules. The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
        :param lcd_w: Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
        :param lcd_h: Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.
        Corresponding Camera Model:
        Number	Camera Model	Communication Method
        0	GC032A	SPI
        1	BF3901	SPI
        """

    def open(self):
        """This method enables the camera code scanning feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def close(self):
        """This method disables the camera code scanning feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def start(self):
        """This method starts the camera code scanning.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def stop(self):
        """This method stops the camera code scanning.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def pause(self):
        """This method pauses the camera code scanning.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def resume(self):
        """This method resumes the camera code scanning.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def callback(self, cb):
        """This method sets the scanning callback function.

        :param cb: Scanning callback function. The prototype is as `cb(result_list)`.
        Parameter of the Callback Function：
            result_list[0] - Integer type. The scanning result. 0 indicates successful execution and other values indicate failed execution.
            result_list[1] - String type. The scanning content.
        :return: 0 - Successful execution; Other values - Failed execution.
        """


class CamCapture(object):
    """Camera Capture

    Class feature: Camera capturing and saving.
    Note: Please initialize the LCD before using this feature.
    Descriptions: https://python.quectel.com/doc/API_reference/en/medialib/camera.CamCapture.html
    """

    def __init__(self, model, cam_w, cam_h, perview_level, lcd_w, lcd_h):
        """Creates a camCapture object.

        :param model: Integer type. Camera model. It can be set to 0 or 1. Click here for corresponding camera model.
        :param cam_w: Integer type. Camera horizontal resolution. Please fill in according to the specifications of the corresponding camera model.
        :param cam_h: Integer type. Camera vertical resolution. Please fill in according to the specifications of the corresponding camera model.
        :param perview_level: Integer type. Preview level. Fill with 1 or 2 on EC600N series, EC800N series, EC600M series and EC800M series modules.The higher the level, the smoother the image, and the more resources consumed. Fill with 1 on other modules.
        :param lcd_w: Integer type. LCD horizontal resolution. Please fill in according to the specifications of the LCD actually used.
        :param lcd_h: Integer type. LCD vertical resolution. Please fill in according to the specifications of the LCD actually used.
        Corresponding Camera Model:
        Number	Camera Model	Communication Method
        0	GC032A	SPI
        1	BF3901	SPI
        """

    def open(self):
        """This method enables the camera capturing feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def close(self):
        """This method disables the camera capturing feature.

        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def start(self, width,  height, pic_name):
        """This method starts capturing and saving the image.

        Note: The capture result is based on the callback function parameters.

        :param width: Integer type. The horizontal resolution of the saved image.
        :param height: Integer type. The vertical resolution of the saved image.
        :param pic_name: String type. The name of the image. You don't have to add .jpeg suffix to the image name as it will be added automatically.
        :return: 0 - Successful execution; Other values - Failed execution.
        """

    def callback(self, cb):
        """This method sets the callback function of camera capturing.

        :param cb: The callback function of camera capture. The prototype is as `cb(result_list)`
        Parameter of the Callback Function：
            result_list[0] - Integer type. The save result. 0 indicates successful execution and other values indicate failed execution.
            result_list[1] - String type. The name of the saved image.
        :return: 0 - Successful execution; Other values - Failed execution.
        """
