"""
Function:
The module contains various audio features, including audio playback, TTS (text-to-speech) playback, recording and so on.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/medialib/audio.html
"""


class Audio(object):
    """Class feature: Audio playback.

    Currently supported modules：EC600N Series, EC800N Series, EC600M-CN(LA/LE), EC800M-CN(LA/LE/GA), EC600U Series, EC200U Series, EG912U, EG915U and EG915N-EUAG.
    Description: https://python.quectel.com/doc/API_reference/en/medialib/audio.Audio.html
    """

    def __init__(self, device):
        """Creates an audio object.

        :param device: Integer type. The output channel. 0 indicates earpiece, 1 indicates headphone and 2 indicates speaker. See the table below for the specific channels supported by each module.
        Channels Supported by the Module:
        Module	Earpiece	Headphone	Speaker
        EC600N series	Supported	Unsupported	Unsupported
        EC800N series	Supported	Unsupported	Unsupported
        EC600M-CN(LA/LE)	Supported	Unsupported	Unsupported
        EC800M-CN(LA/LE/GA)	Supported	Unsupported	Unsupported
        EG915N	Supported	Unsupported	Unsupported
        EG912N	Supported	Unsupported	Unsupported
        EG912U	Supported	Unsupported	Unsupported
        EC200U series	Unsupported	Unsupported	Supported
        EC600U series	Supported	Supported	Supported
        EG915U	Supported	Supported	Unsupported
        """

    def set_pa(self, gpio, num):
        """This method sets the GPIO of the output PA.

        :param gpio: Integer type. The output GPIO. Refer to Pin.
        :param num: Integer type. Number of power-on pulses.
        :return: 1- Successful execution; 0- Failed execution.
        """

    def play(self, priority, breakin, filename):
        """This method plays audio files.

        It supports the playback of MP3, AMR, and WAV format files. Priorities from 0 to 4 are supported, with a higher number indicating a higher priority. Each priority group supports up to 10 playback tasks simultaneously, and the same playback queue is shared with TTS playback.

        Note: Since the TTS and audio file playback share the same playback queue, the playback priority and interruption mode set in the TTS are not only compared with those set in other TTS playback tasks, but also with those set in audio file playback tasks. Similarly, the playback priority and interruption mode set in audio file playback are also valid for those set in TTS tasks.

        Description of the Playback Path:
        The user partition path is fixed to start with 'U:/', representing the root directory of the user partition. If the user creates an "audio" directory in the root directory and stores the audio files in the "audio" directory, then the path parameter passed in the playback interface should be 'U:/audio/music.mp3'.

        :param priority: Integer type. Playback priority. Supports priorities from 0 to 4, with a higher number indicating a higher priority.
        :param breakin: Integer type. Interruption mode. 0 indicates the playback is not allowed to be interrupted and 1 indicates the playback is allowed to be interrupted.
        :param filename: Mode. String type. The name of the file to be played, including the file storage path. Click here for the description of the playback path.
        :return:
        0 - Successful execution
        -1- Failed execution
        1 - The task cannot be played immediately and is added to the playback queue.
        -2- The task can neither be played immediately nor added to the playback queue because the task queue of the priority group for the request has reached its limit.
        """

    def stop(self):
        """This method stops the audio that is currently playing.

        :return: 0 - Successful execution; -1- Failed execution.
        """

    def stopAll(self):
        """This method stops the playback of the entire queue.

        That is, if an audio file is currently being played and there are other audio files waiting to be played in the queue, calling this method will not only stop the current playback but also clear the entire queue and no more content is played. If an audio file is currently being played and the playback queue is empty, calling this method is as same as calling Audio.stop().

        :return: 0 - Successful execution; -1- Failed execution.
        """

    def setCallback(self, cb):
        """This method registers the user's callback function to notify the user of the playback status of the audio file.

        Note: It is recommended to only perform simple and short operations instead of time-consuming or blocking operations in this callback function.

        :param cb: Function type. User callback function. The prototype is as `cb(event)`
        Parameter of the Callback Function：
            event - Integer type. Playback status. click here for the description of this parameter.
        Description of Parameter `event`
        event	Status
        0	Start playback
        7	Playback complete
        :return:0 - Successful execution; -1 - Failed execution.
        """

    def getState(self):
        """This method gets the audio initialization state.

        :return: 0 - Successful initialization; -1 - Failed initialization.
        """

    def getVolume(self):
        """This method gets the current playback volume. Range: 0–11. 0 indicates mute. Default value: 7.

        :return: Volume value in integer type.
        """

    def setVolume(self, vol):
        """This method sets the playback volume. Range: 0–11. 0 indicates mute.

        :param vol: Integer type. Playback volume. Range: 0–11.
        :return: 0 - Successful execution; -1 - Failed execution.
        """

    def playStream(self, format, buf):
        """This method plays audio stream. It supports audio stream in MP3, AMR, and WAV format.

        :param format: Integer type. The audio stream format. 2 - WAVPCM，3 - MP3，4 - AMRNB.
        :param buf: Binary file. The content of the audio stream.
        :return: 0 - Successful execution; -1 - Failed execution.
        """

    def stopPlayStream(self):
        """This method stops playing the audio stream.

        :return: 0 - Successful execution; -1 - Failed execution.
        """

    def aud_tone_play(self, tone, time):
        """This method plays tone, and automatically stops playing after playing for a period of time.

        For EC600N/EC800N series module, the value is immediately returned after calling this method. For EC600U/EC200U series module, the return value is in blocked and wait status.

        :param tone: Integer type. The type of tone. Range: 0–15. Key tone (0~9, A, B, C, D, #, *)，16: dialing tone.
        :param time: Integer type. Playback time. Unit: ms. 0 indicates always playing without stopping.
        :return: 0 - Successful execution; -1 - Failed execution.
        """

    def aud_tone_play_stop(self):
        """This method actively stops playing the key tones.

        :return: 0 - Successful execution; -1- Failed execution.
        """


class Record(object):
    """Class feature: Recording.

    Currently supported models: EC600N Series, EC800N Series, EC600M-CN(LA/LE), EC800M-CN(LA/LE/GA), EC600U Series, EC200U Series, EG912U, EG915U and EG915N-EUAG.
    Description: https://python.quectel.com/doc/API_reference/en/medialib/audio.Record.html
    """

    def __init__(self, device):
        """Creates a record object.

        If a parameter is passed, it should be consistent with the parameter of audio.Audio(device).

        :param device: Integer type. The output channel. 0 indicates earpiece, 1 indicates headphone and 2 indicates speaker. Default value: 0. See the table below for the specific channels supported by each module.

        Channels Supported by the Module:
        Module Series	Earpiece	Headphone	Speaker
        EC600N Series	Supported	Unsupported	Unsupported
        EC800N Series	Supported	Unsupported	Unsupported
        EC600M-CN(LA/LE)	Supported	Unsupported	Unsupported
        EC800M-CN(LA/LE/GA)	Supported	Unsupported	Unsupported
        EG915N	Supported	Unsupported	Unsupported
        EG912N	Supported	Unsupported	Unsupported
        EG912U	Supported	Unsupported	Unsupported
        EC200U Series	Unsupported	Unsupported	Supported
        EC600U Series	Supported	Supported	Supported
        EG915U	Supported	Supported	Unsupported
        """

    def start(self, file_name, seconds):
        """This method starts recording.

        :param file_name: String type. Name of the recording file.
        :param seconds: Integer type. Recording duration. Unit: second.
        :return:
        0 - Successful execution
        -1 - Failed to overwrite the file
        -2 - Failed to open the file
        -3 - The file is in use.
        -4 - Channel setting error
        -5 - Timer resource request failure
        -6 - Audio format error
        """

    def stop(self):
        """This method stops recording.

        :return: 0 - Successful execution; -1 - Failed execution.
        """

    def getFilePath(self, file_name):
        """This method reads the path of the recording file.

        :param file_name: String type. Name of the recording file.
        :return: Returns the recording file path for successful execution.
        -1 - The target file does not exist.
        -2- The file name length is 0.
        """

    def getData(self, file_name, offset, size):
        """This method reads the recording data.

        :param file_name: String type. The name of the recording file.
        :param offset: Integer type. The offset of the data to be read.
        :param size: Integer type. Data size. Unit: byte. The size should be less than 10 KB.
        :return: Returns the recording data (bytearray type) for successful execution.
        The following are return values for failed execution:
        -1 - Failed to read the data.
        -2 - Failed to open the file.
        -3 - Failed to set the offset.
        -4 - The file is in use.
        -5 - The setting is beyond the file size (offset+size > file_size).
        -6 - The data size to be read is greater than 10 KB.
        -7 - The memory is less than 10 K.
        """

    def getSize(self, file_name):
        """This method reads the size of the recording file.

        :param file_name: String type. The name of the recording file.
        :return: Returns the file size for successful execution. Unit: byte. (EC600N series, EC800N series, EC800M series, EC600M series, and EG915N modules do not return file headers).
        The return values for failed execution are as follows:
        -1 - Failed to get the file size.
        -2 - Failed to open the file.
        -3 - The file is in use.
        -4 - The file name length is 0.
        For WAV format, this value is 44 bytes larger than the callback return value (44 bytes is the file header); for AMR format, this value is 6 bytes larger than the callback return value (6 bytes is the file header).
        """

    def Delete(self, file_name):
        """This method deletes the recording file.

        :param file_name: String type. The name of the recording file.
        :return:
        0 - Successful execution
        -1 - The file does not exist.
        -2 - The file is in use.
        """

    def exists(self, file_name):
        """This method determines whether the recording file exists.

        :param file_name: String type. The name of the recording file.
        :return: True - The file exists. False - The file does not exist.
        """

    def isBusy(self):
        """This method determines whether recording is in progress.

        :return: 0 - Not in progress; 1 - In progress.
        """

    def end_callback(self, cb):
        """This method sets the callback function for the end of the recording.

        :param cb: Function type. Callback function for the end of the recording. The prototype is as `cb(audio_msg)`
        Parameter of the Callback Function：
        audio_msg - List type. The recording information. The elements are as follows:
        audio_msg[0]：file_path. String type. The file path.
        audio_msg[1]：audio_len. Integer type. The recording length.
        audio_msg[2]：audio_state. Integer type. The recording status. Click here for the description of audio_state of the callback function.
        :return: 0 - Successful execution; -1 -Failed execution.
        Description of audio_state：
        event	Description
        -1	Failure
        0	Start playback
        3	Playback ends
        """

    def gain(self, code_gain, dsp_gain):
        """This method sets the recording gain.

        Currently, only the EC600N/EC800N series modules support this function.

        :param code_gain: Integer type. Uplink codec gain. Range: [0,4].
        :param dsp_gain: Integer type. Uplink digital gain. Range: [-36,12].
        :return: 0 - Successful execution; -1- Failed execution.
        """

    def amrEncDtx_enable(self, on_off=None):
        """This method controls the DTX feature of the AMR recording.

        Currently, only the EC600N/EC800N series modules support this feature.

        :param on_off: Integer type. Enable or disable the DTX feature. 1- Enable; 0- Disable. No parameter passed - get the current configuration
        :return: No parameter passed, return the current configuration. The parameter is passed: no return value if the parameter is correct, and an exception is thrown if the parameter is incorrect.
        """

    def stream_start(self, format, samplerate, time):
        """This method starts recording audio streams.

        Note that when recording an audio stream, read the audio stream timely. Currently, a loop buffer is used. Failure to read the audio stream in time will result in data loss.
        Currently, only the EC200U/EC600U series modules support this function.

        :param format: Integer type. Audio format. Currently supports AMR format. See constant.
        :param samplerate: Integer type. Sample rate. Currently supports 8000 sps and 16000 sps.
        :param time: Integer type. Recording duration. Unit: second.
        :return: 0 - Successful execution. -1- Failed execution.
        """

    def stream_read(self, read_buf, len):
        """This method reads the recording stream.

        Currently, only the EC600N/EC800N series modules support this feature.

        :param read_buf: Bytearray type. Recording stream buffer.
        :param len: Integer type. Length to be read.
        :return: Returns the number of bytes actually read for successful execution or -1 if failed.
        """

    AMRNB: int = ...  # AMR format.
