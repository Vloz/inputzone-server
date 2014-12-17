# -*- coding: utf8 -*-
__author__ = 'vloz'

from google.appengine.ext import ndb
from google.appengine.ext.ndb import metadata

class Converter(ndb.Model):
    title = ndb.StringProperty(indexed=True, required=True)
    hasPnacl = ndb.BooleanProperty(indexed=False, default=False)
    hasEmscr = ndb.BooleanProperty(indexed=False, default=False)
    inputExt = ndb.StringProperty(indexed=False, default="")
    pnaclBin = ndb.StringProperty(indexed=False)
    emscrBin = ndb.StringProperty(indexed=False)
    isolated = ndb.BooleanProperty(indexed=False)
    chdir = ndb.StringProperty(indexed=False)
    naclSize = ndb.IntegerProperty(indexed=False)
    fullDesc = ndb.StringProperty(indexed=False)
    shortDesc = ndb.StringProperty(indexed=False)
    inTag = ndb.StringProperty(repeated=True, indexed=True)
    ouTag = ndb.StringProperty(repeated=True, indexed=True)
    footer = ndb.StringProperty(indexed=False)

    @staticmethod
    def init():
        init_list = [
            Converter(id="ffmpeg",
                      title="ffmpeg beta",
                      pnaclBin="converters/ffmpeg/bin/ffmpeg.pexe.nmf",
                      isolated=True,
                      chdir="/",
                      naclSize=10312460,
                      fullDesc="""Convert mp4,webm,mkv,mp3 and others Audio/Video
                       with your web browser without sending any data.""",
                      shortDesc="Convert your audio/video files",
                      ouTag=["h264", "vp8", "vp9", "mkv", "mp4", "webm", "avi", "xvid", "mpg", "mp3",
                             "wav", "oga", "ogv", "mpeg2", "flv"],
                      footer="Version 2.1.3 - Original code by ffmpegTeam"
                      ),
            Converter(id="unecm",
                      title="unecm",
                      inputExt=".ecm",
                      pnaclBin="converters/unecm/bin/unecm.pexe.nmf",
                      emscrBin="converters/unecm/bin/unecm.js",
                      fullDesc="""Convert .ecm images to playstation iso/bin
                      with your web browser without sending any data.""",
                      shortDesc="Convert ecm file to disk images",
                      inTag=["ecm"],
                      ouTag=["iso", "bin"],
                      footer="Original code by Neill Corlett ©2002"
                      ),
            Converter(id="ecmify",
                      title="ecmify",
                      inputExt=".iso,.bin",
                      pnaclBin="converters/ecmify/bin/ecmify.pexe.nmf",
                      fullDesc="""Optimize your iso/bin disk error to make it
                       more compressible with your web browser.""",
                      shortDesc="Make your CD image files more compressible",
                      inTag=["iso", "bin"],
                      ouTag=["ecm"],
                      footer="Original code by Neill Corlett ©2002"
                      ),
            Converter(id="cwebp",
                      title="cwebp",
                      inputExt=".png,.jpg,.tiff,.webp",
                      pnaclBin="converters/webp/bin/cwebp.pexe.nmf",
                      fullDesc="""Convert your jpeg,png,tiff images into Webp
                      with your web browser without sending any data.""",
                      shortDesc="Convert jpeg/png/tiff to webp image",
                      inTag=["jpeg", "png", "tiff", "webp"],
                      ouTag=["webp"],
                      footer="Version 0.4.2 - Original code by WebP team, licensed under the same terms as WebM"
                      ),
            Converter(id="dwebp",
                      title="dwebp",
                      inputExt=".webp",
                      pnaclBin="converters/webp/bin/dwebp.pexe.nmf",
                      fullDesc="""Convert your webp images into png,tiff,bmp
                      with your web browser without sending any data.""",
                      shortDesc="Convert webp to png/tiff image",
                      inTag=["webp"],
                      ouTag=["png", "tiff", "bmp", "pam", "ppm", "pgm", "yuv"],
                      footer="Version 0.4.2 - Original code by WebP team, licensed under the same terms as WebM"
                      )
        ]

        first_init = "Converter" not in metadata.get_kinds()

        for c in init_list:
            c.hasPnacl = c.pnaclBin is not None and c.pnaclBin != ""
            c.hasEmscr = c.emscrBin is not None and c.emscrBin != ""
            if first_init or Converter.get_by_id(c.key.id()) is None:
                c.put()


    # def __init__(self, title, urlname, inputext="", pnaclbin="", emscrbin = "", isolated = False, chdir = "",
    #              naclsize = 0, fulldesc = "", shortdesc = "", intag = None, outag = None ):
    #     ndb.Model.ini
    #     if pnaclbin != "":
    #         self.hasPnacl = True
    #     if emscrbin != "":
    #         self.hasEmscr = True
    #     self.title = title
    #     self.idName = urlname
    #     if inputext != "":
    #         self.inputExt = inputext
    #     self.pnaclBin = pnaclbin
    #     self.emscrBin = emscrbin
    #     self.isolated = isolated
    #     if chdir != "":
    #         self.chdir = chdir
    #     self.naclSize = naclsize
    #     self.fullDesc = fulldesc
    #     self.shortDesc = shortdesc
    #     if intag is not None:
    #         self.inTag = intag
    #     if outag is not None:
    #         self.ouTag = outag

