# ----------------------------------------------------------------------------
# pyglet
# Copyright (c) 2006-2007 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------
'''Wrapper for /usr/include/GL/glx.h

Do not modify generated portions of this file.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: glx.py 878 2007-06-09 04:58:51Z Alex.Holkner $'

from ctypes import *
from pyglet.gl.lib import link_GLX as _link_function
from pyglet.gl.lib import c_ptrdiff_t, c_void

if not _link_function:
    raise ImportError('libGL.so is not available.')

# BEGIN GENERATED CONTENT (do not edit below this line)

# This content is generated by tools/gengl.py.
# Wrapper for /usr/include/GL/glx.h


GLX_USE_GL = 1 	# /usr/include/GL/glx.h:36
GLX_BUFFER_SIZE = 2 	# /usr/include/GL/glx.h:37
GLX_LEVEL = 3 	# /usr/include/GL/glx.h:38
GLX_RGBA = 4 	# /usr/include/GL/glx.h:39
GLX_DOUBLEBUFFER = 5 	# /usr/include/GL/glx.h:40
GLX_STEREO = 6 	# /usr/include/GL/glx.h:41
GLX_AUX_BUFFERS = 7 	# /usr/include/GL/glx.h:42
GLX_RED_SIZE = 8 	# /usr/include/GL/glx.h:43
GLX_GREEN_SIZE = 9 	# /usr/include/GL/glx.h:44
GLX_BLUE_SIZE = 10 	# /usr/include/GL/glx.h:45
GLX_ALPHA_SIZE = 11 	# /usr/include/GL/glx.h:46
GLX_DEPTH_SIZE = 12 	# /usr/include/GL/glx.h:47
GLX_STENCIL_SIZE = 13 	# /usr/include/GL/glx.h:48
GLX_ACCUM_RED_SIZE = 14 	# /usr/include/GL/glx.h:49
GLX_ACCUM_GREEN_SIZE = 15 	# /usr/include/GL/glx.h:50
GLX_ACCUM_BLUE_SIZE = 16 	# /usr/include/GL/glx.h:51
GLX_ACCUM_ALPHA_SIZE = 17 	# /usr/include/GL/glx.h:52
GLX_BAD_SCREEN = 1 	# /usr/include/GL/glx.h:58
GLX_BAD_ATTRIBUTE = 2 	# /usr/include/GL/glx.h:59
GLX_NO_EXTENSION = 3 	# /usr/include/GL/glx.h:60
GLX_BAD_VISUAL = 4 	# /usr/include/GL/glx.h:61
GLX_BAD_CONTEXT = 5 	# /usr/include/GL/glx.h:62
GLX_BAD_VALUE = 6 	# /usr/include/GL/glx.h:63
GLX_BAD_ENUM = 7 	# /usr/include/GL/glx.h:64
GLX_VENDOR = 1 	# /usr/include/GL/glx.h:69
GLX_VERSION = 2 	# /usr/include/GL/glx.h:70
GLX_EXTENSIONS = 3 	# /usr/include/GL/glx.h:71
# VERSION_1_3 (/usr/include/GL/glx.h:73)
GLX_WINDOW_BIT = 1 	# /usr/include/GL/glx.h:74
GLX_PIXMAP_BIT = 2 	# /usr/include/GL/glx.h:75
GLX_PBUFFER_BIT = 4 	# /usr/include/GL/glx.h:76
GLX_RGBA_BIT = 1 	# /usr/include/GL/glx.h:77
GLX_COLOR_INDEX_BIT = 2 	# /usr/include/GL/glx.h:78
GLX_PBUFFER_CLOBBER_MASK = 134217728 	# /usr/include/GL/glx.h:79
GLX_FRONT_LEFT_BUFFER_BIT = 1 	# /usr/include/GL/glx.h:80
GLX_FRONT_RIGHT_BUFFER_BIT = 2 	# /usr/include/GL/glx.h:81
GLX_BACK_LEFT_BUFFER_BIT = 4 	# /usr/include/GL/glx.h:82
GLX_BACK_RIGHT_BUFFER_BIT = 8 	# /usr/include/GL/glx.h:83
GLX_AUX_BUFFERS_BIT = 16 	# /usr/include/GL/glx.h:84
GLX_DEPTH_BUFFER_BIT = 32 	# /usr/include/GL/glx.h:85
GLX_STENCIL_BUFFER_BIT = 64 	# /usr/include/GL/glx.h:86
GLX_ACCUM_BUFFER_BIT = 128 	# /usr/include/GL/glx.h:87
GLX_CONFIG_CAVEAT = 32 	# /usr/include/GL/glx.h:88
GLX_X_VISUAL_TYPE = 34 	# /usr/include/GL/glx.h:89
GLX_TRANSPARENT_TYPE = 35 	# /usr/include/GL/glx.h:90
GLX_TRANSPARENT_INDEX_VALUE = 36 	# /usr/include/GL/glx.h:91
GLX_TRANSPARENT_RED_VALUE = 37 	# /usr/include/GL/glx.h:92
GLX_TRANSPARENT_GREEN_VALUE = 38 	# /usr/include/GL/glx.h:93
GLX_TRANSPARENT_BLUE_VALUE = 39 	# /usr/include/GL/glx.h:94
GLX_TRANSPARENT_ALPHA_VALUE = 40 	# /usr/include/GL/glx.h:95
GLX_DONT_CARE = 4294967295 	# /usr/include/GL/glx.h:96
GLX_NONE = 32768 	# /usr/include/GL/glx.h:97
GLX_SLOW_CONFIG = 32769 	# /usr/include/GL/glx.h:98
GLX_TRUE_COLOR = 32770 	# /usr/include/GL/glx.h:99
GLX_DIRECT_COLOR = 32771 	# /usr/include/GL/glx.h:100
GLX_PSEUDO_COLOR = 32772 	# /usr/include/GL/glx.h:101
GLX_STATIC_COLOR = 32773 	# /usr/include/GL/glx.h:102
GLX_GRAY_SCALE = 32774 	# /usr/include/GL/glx.h:103
GLX_STATIC_GRAY = 32775 	# /usr/include/GL/glx.h:104
GLX_TRANSPARENT_RGB = 32776 	# /usr/include/GL/glx.h:105
GLX_TRANSPARENT_INDEX = 32777 	# /usr/include/GL/glx.h:106
GLX_VISUAL_ID = 32779 	# /usr/include/GL/glx.h:107
GLX_SCREEN = 32780 	# /usr/include/GL/glx.h:108
GLX_NON_CONFORMANT_CONFIG = 32781 	# /usr/include/GL/glx.h:109
GLX_DRAWABLE_TYPE = 32784 	# /usr/include/GL/glx.h:110
GLX_RENDER_TYPE = 32785 	# /usr/include/GL/glx.h:111
GLX_X_RENDERABLE = 32786 	# /usr/include/GL/glx.h:112
GLX_FBCONFIG_ID = 32787 	# /usr/include/GL/glx.h:113
GLX_RGBA_TYPE = 32788 	# /usr/include/GL/glx.h:114
GLX_COLOR_INDEX_TYPE = 32789 	# /usr/include/GL/glx.h:115
GLX_MAX_PBUFFER_WIDTH = 32790 	# /usr/include/GL/glx.h:116
GLX_MAX_PBUFFER_HEIGHT = 32791 	# /usr/include/GL/glx.h:117
GLX_MAX_PBUFFER_PIXELS = 32792 	# /usr/include/GL/glx.h:118
GLX_PRESERVED_CONTENTS = 32795 	# /usr/include/GL/glx.h:119
GLX_LARGEST_PBUFFER = 32796 	# /usr/include/GL/glx.h:120
GLX_WIDTH = 32797 	# /usr/include/GL/glx.h:121
GLX_HEIGHT = 32798 	# /usr/include/GL/glx.h:122
GLX_EVENT_MASK = 32799 	# /usr/include/GL/glx.h:123
GLX_DAMAGED = 32800 	# /usr/include/GL/glx.h:124
GLX_SAVED = 32801 	# /usr/include/GL/glx.h:125
GLX_WINDOW = 32802 	# /usr/include/GL/glx.h:126
GLX_PBUFFER = 32803 	# /usr/include/GL/glx.h:127
GLX_PBUFFER_HEIGHT = 32832 	# /usr/include/GL/glx.h:128
GLX_PBUFFER_WIDTH = 32833 	# /usr/include/GL/glx.h:129
# VERSION_1_4 (/usr/include/GL/glx.h:132)
GLX_SAMPLE_BUFFERS = 100000 	# /usr/include/GL/glx.h:133
GLX_SAMPLES = 100001 	# /usr/include/GL/glx.h:134
# ARB_get_proc_address (/usr/include/GL/glx.h:137)
__GLXextFuncPtr = CFUNCTYPE(None) 	# /usr/include/GL/glx.h:138
XID = c_ulong 	# /usr/include/X11/X.h:71
GLXContextID = XID 	# /usr/include/GL/glx.h:144
GLXPixmap = XID 	# /usr/include/GL/glx.h:145
GLXDrawable = XID 	# /usr/include/GL/glx.h:146
GLXPbuffer = XID 	# /usr/include/GL/glx.h:147
GLXPbufferSGIX = XID 	# /usr/include/GL/glx.h:148
GLXWindow = XID 	# /usr/include/GL/glx.h:149
GLXFBConfigID = XID 	# /usr/include/GL/glx.h:150
class struct___GLXcontextRec(Structure):
    __slots__ = [
    ]
struct___GLXcontextRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXContext = POINTER(struct___GLXcontextRec) 	# /usr/include/GL/glx.h:155
class struct___GLXFBConfigRec(Structure):
    __slots__ = [
    ]
struct___GLXFBConfigRec._fields_ = [
    ('_opaque_struct', c_int)
]

GLXFBConfig = POINTER(struct___GLXFBConfigRec) 	# /usr/include/GL/glx.h:160
class struct_anon_94(Structure):
    __slots__ = [
        'visual',
        'visualid',
        'screen',
        'depth',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'colormap_size',
        'bits_per_rgb',
    ]
class struct_anon_11(Structure):
    __slots__ = [
        'ext_data',
        'visualid',
        'class',
        'red_mask',
        'green_mask',
        'blue_mask',
        'bits_per_rgb',
        'map_entries',
    ]
class struct__XExtData(Structure):
    __slots__ = [
        'number',
        'next',
        'free_private',
        'private_data',
    ]
XPointer = c_char_p 	# /usr/include/X11/Xlib.h:108
struct__XExtData._fields_ = [
    ('number', c_int),
    ('next', POINTER(struct__XExtData)),
    ('free_private', POINTER(CFUNCTYPE(c_int, POINTER(struct__XExtData)))),
    ('private_data', XPointer),
]

XExtData = struct__XExtData 	# /usr/include/X11/Xlib.h:187
VisualID = c_ulong 	# /usr/include/X11/X.h:81
struct_anon_11._fields_ = [
    ('ext_data', POINTER(XExtData)),
    ('visualid', VisualID),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('bits_per_rgb', c_int),
    ('map_entries', c_int),
]

Visual = struct_anon_11 	# /usr/include/X11/Xlib.h:270
struct_anon_94._fields_ = [
    ('visual', POINTER(Visual)),
    ('visualid', VisualID),
    ('screen', c_int),
    ('depth', c_int),
    ('class', c_int),
    ('red_mask', c_ulong),
    ('green_mask', c_ulong),
    ('blue_mask', c_ulong),
    ('colormap_size', c_int),
    ('bits_per_rgb', c_int),
]

XVisualInfo = struct_anon_94 	# /usr/include/X11/Xutil.h:296
class struct__XDisplay(Structure):
    __slots__ = [
    ]
struct__XDisplay._fields_ = [
    ('_opaque_struct', c_int)
]

Display = struct__XDisplay 	# /usr/include/X11/Xlib.h:519
# /usr/include/GL/glx.h:168
glXChooseVisual = _link_function('glXChooseVisual', POINTER(XVisualInfo), [POINTER(Display), c_int, POINTER(c_int)], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:171
glXCopyContext = _link_function('glXCopyContext', None, [POINTER(Display), GLXContext, GLXContext, c_ulong], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:174
glXCreateContext = _link_function('glXCreateContext', GLXContext, [POINTER(Display), POINTER(XVisualInfo), GLXContext, c_int], 'ARB_get_proc_address')

Pixmap = XID 	# /usr/include/X11/X.h:107
# /usr/include/GL/glx.h:177
glXCreateGLXPixmap = _link_function('glXCreateGLXPixmap', GLXPixmap, [POINTER(Display), POINTER(XVisualInfo), Pixmap], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:180
glXDestroyContext = _link_function('glXDestroyContext', None, [POINTER(Display), GLXContext], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:182
glXDestroyGLXPixmap = _link_function('glXDestroyGLXPixmap', None, [POINTER(Display), GLXPixmap], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:184
glXGetConfig = _link_function('glXGetConfig', c_int, [POINTER(Display), POINTER(XVisualInfo), c_int, POINTER(c_int)], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:187
glXGetCurrentContext = _link_function('glXGetCurrentContext', GLXContext, [], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:189
glXGetCurrentDrawable = _link_function('glXGetCurrentDrawable', GLXDrawable, [], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:191
glXIsDirect = _link_function('glXIsDirect', c_int, [POINTER(Display), GLXContext], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:193
glXMakeCurrent = _link_function('glXMakeCurrent', c_int, [POINTER(Display), GLXDrawable, GLXContext], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:196
glXQueryExtension = _link_function('glXQueryExtension', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:198
glXQueryVersion = _link_function('glXQueryVersion', c_int, [POINTER(Display), POINTER(c_int), POINTER(c_int)], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:200
glXSwapBuffers = _link_function('glXSwapBuffers', None, [POINTER(Display), GLXDrawable], 'ARB_get_proc_address')

Font = XID 	# /usr/include/X11/X.h:105
# /usr/include/GL/glx.h:202
glXUseXFont = _link_function('glXUseXFont', None, [Font, c_int, c_int, c_int], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:204
glXWaitGL = _link_function('glXWaitGL', None, [], 'ARB_get_proc_address')

# /usr/include/GL/glx.h:206
glXWaitX = _link_function('glXWaitX', None, [], 'ARB_get_proc_address')

# VERSION_1_1 (/usr/include/GL/glx.h:209)
GLX_VERSION_1_1 = 1 	# /usr/include/GL/glx.h:210
# /usr/include/GL/glx.h:214
glXGetClientString = _link_function('glXGetClientString', c_char_p, [POINTER(Display), c_int], 'VERSION_1_1')

# /usr/include/GL/glx.h:216
glXQueryServerString = _link_function('glXQueryServerString', c_char_p, [POINTER(Display), c_int, c_int], 'VERSION_1_1')

# /usr/include/GL/glx.h:218
glXQueryExtensionsString = _link_function('glXQueryExtensionsString', c_char_p, [POINTER(Display), c_int], 'VERSION_1_1')

# VERSION_1_2 (/usr/include/GL/glx.h:222)
GLX_VERSION_1_2 = 1 	# /usr/include/GL/glx.h:223
# /usr/include/GL/glx.h:227
glXGetCurrentDisplay = _link_function('glXGetCurrentDisplay', POINTER(Display), [], 'VERSION_1_2')

# VERSION_1_3 (/usr/include/GL/glx.h:230)
GLX_VERSION_1_3 = 1 	# /usr/include/GL/glx.h:231
# /usr/include/GL/glx.h:235
glXChooseFBConfig = _link_function('glXChooseFBConfig', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:238
glXCreateNewContext = _link_function('glXCreateNewContext', GLXContext, [POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int], 'VERSION_1_3')

# /usr/include/GL/glx.h:242
glXCreatePbuffer = _link_function('glXCreatePbuffer', GLXPbuffer, [POINTER(Display), GLXFBConfig, POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:245
glXCreatePixmap = _link_function('glXCreatePixmap', GLXPixmap, [POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)], 'VERSION_1_3')

Window = XID 	# /usr/include/X11/X.h:101
# /usr/include/GL/glx.h:248
glXCreateWindow = _link_function('glXCreateWindow', GLXWindow, [POINTER(Display), GLXFBConfig, Window, POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:251
glXDestroyPbuffer = _link_function('glXDestroyPbuffer', None, [POINTER(Display), GLXPbuffer], 'VERSION_1_3')

# /usr/include/GL/glx.h:253
glXDestroyPixmap = _link_function('glXDestroyPixmap', None, [POINTER(Display), GLXPixmap], 'VERSION_1_3')

# /usr/include/GL/glx.h:255
glXDestroyWindow = _link_function('glXDestroyWindow', None, [POINTER(Display), GLXWindow], 'VERSION_1_3')

# /usr/include/GL/glx.h:257
glXGetCurrentReadDrawable = _link_function('glXGetCurrentReadDrawable', GLXDrawable, [], 'VERSION_1_3')

# /usr/include/GL/glx.h:259
glXGetFBConfigAttrib = _link_function('glXGetFBConfigAttrib', c_int, [POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:262
glXGetFBConfigs = _link_function('glXGetFBConfigs', POINTER(GLXFBConfig), [POINTER(Display), c_int, POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:264
glXGetSelectedEvent = _link_function('glXGetSelectedEvent', None, [POINTER(Display), GLXDrawable, POINTER(c_ulong)], 'VERSION_1_3')

# /usr/include/GL/glx.h:267
glXGetVisualFromFBConfig = _link_function('glXGetVisualFromFBConfig', POINTER(XVisualInfo), [POINTER(Display), GLXFBConfig], 'VERSION_1_3')

# /usr/include/GL/glx.h:269
glXMakeContextCurrent = _link_function('glXMakeContextCurrent', c_int, [POINTER(Display), GLXDrawable, GLXDrawable, GLXContext], 'VERSION_1_3')

# /usr/include/GL/glx.h:272
glXQueryContext = _link_function('glXQueryContext', c_int, [POINTER(Display), GLXContext, c_int, POINTER(c_int)], 'VERSION_1_3')

# /usr/include/GL/glx.h:275
glXQueryDrawable = _link_function('glXQueryDrawable', None, [POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)], 'VERSION_1_3')

# /usr/include/GL/glx.h:278
glXSelectEvent = _link_function('glXSelectEvent', None, [POINTER(Display), GLXDrawable, c_ulong], 'VERSION_1_3')

PFNGLXGETFBCONFIGSPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:281
PFNGLXCHOOSEFBCONFIGPROC = CFUNCTYPE(POINTER(GLXFBConfig), POINTER(Display), c_int, POINTER(c_int), POINTER(c_int)) 	# /usr/include/GL/glx.h:282
PFNGLXGETFBCONFIGATTRIBPROC = CFUNCTYPE(c_int, POINTER(Display), GLXFBConfig, c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:283
PFNGLXGETVISUALFROMFBCONFIGPROC = CFUNCTYPE(POINTER(XVisualInfo), POINTER(Display), GLXFBConfig) 	# /usr/include/GL/glx.h:284
PFNGLXCREATEWINDOWPROC = CFUNCTYPE(GLXWindow, POINTER(Display), GLXFBConfig, Window, POINTER(c_int)) 	# /usr/include/GL/glx.h:285
PFNGLXDESTROYWINDOWPROC = CFUNCTYPE(None, POINTER(Display), GLXWindow) 	# /usr/include/GL/glx.h:286
PFNGLXCREATEPIXMAPPROC = CFUNCTYPE(GLXPixmap, POINTER(Display), GLXFBConfig, Pixmap, POINTER(c_int)) 	# /usr/include/GL/glx.h:287
PFNGLXDESTROYPIXMAPPROC = CFUNCTYPE(None, POINTER(Display), GLXPixmap) 	# /usr/include/GL/glx.h:288
PFNGLXCREATEPBUFFERPROC = CFUNCTYPE(GLXPbuffer, POINTER(Display), GLXFBConfig, POINTER(c_int)) 	# /usr/include/GL/glx.h:289
PFNGLXDESTROYPBUFFERPROC = CFUNCTYPE(None, POINTER(Display), GLXPbuffer) 	# /usr/include/GL/glx.h:290
PFNGLXQUERYDRAWABLEPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_int, POINTER(c_uint)) 	# /usr/include/GL/glx.h:291
PFNGLXCREATENEWCONTEXTPROC = CFUNCTYPE(GLXContext, POINTER(Display), GLXFBConfig, c_int, GLXContext, c_int) 	# /usr/include/GL/glx.h:292
PFNGLXMAKECONTEXTCURRENTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXDrawable, GLXDrawable, GLXContext) 	# /usr/include/GL/glx.h:293
PFNGLXGETCURRENTREADDRAWABLEPROC = CFUNCTYPE(GLXDrawable) 	# /usr/include/GL/glx.h:294
PFNGLXGETCURRENTDISPLAYPROC = CFUNCTYPE(POINTER(Display)) 	# /usr/include/GL/glx.h:295
PFNGLXQUERYCONTEXTPROC = CFUNCTYPE(c_int, POINTER(Display), GLXContext, c_int, POINTER(c_int)) 	# /usr/include/GL/glx.h:296
PFNGLXSELECTEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, c_ulong) 	# /usr/include/GL/glx.h:297
PFNGLXGETSELECTEDEVENTPROC = CFUNCTYPE(None, POINTER(Display), GLXDrawable, POINTER(c_ulong)) 	# /usr/include/GL/glx.h:298
# VERSION_1_4 (/usr/include/GL/glx.h:302)
GLX_VERSION_1_4 = 1 	# /usr/include/GL/glx.h:303
GLubyte = c_ubyte 	# /usr/include/GL/gl.h:60
# /usr/include/GL/glx.h:307
glXGetProcAddress = _link_function('glXGetProcAddress', __GLXextFuncPtr, [POINTER(GLubyte)], 'VERSION_1_4')

PFNGLXGETPROCADDRESSPROC = CFUNCTYPE(__GLXextFuncPtr, POINTER(GLubyte)) 	# /usr/include/GL/glx.h:308
# ARB_get_proc_address (/usr/include/GL/glx.h:318)
GLX_ARB_get_proc_address = 1 	# /usr/include/GL/glx.h:319
# /usr/include/GL/glx.h:321
glXGetProcAddressARB = _link_function('glXGetProcAddressARB', POINTER(CFUNCTYPE(None)), [POINTER(GLubyte)], 'ARB_get_proc_address')

PFNGLXGETPROCADDRESSARBPROC = CFUNCTYPE(__GLXextFuncPtr, POINTER(GLubyte)) 	# /usr/include/GL/glx.h:322
class struct_anon_96(Structure):
    __slots__ = [
        'event_type',
        'draw_type',
        'serial',
        'send_event',
        'display',
        'drawable',
        'buffer_mask',
        'aux_buffer',
        'x',
        'y',
        'width',
        'height',
        'count',
    ]
struct_anon_96._fields_ = [
    ('event_type', c_int),
    ('draw_type', c_int),
    ('serial', c_ulong),
    ('send_event', c_int),
    ('display', POINTER(Display)),
    ('drawable', GLXDrawable),
    ('buffer_mask', c_uint),
    ('aux_buffer', c_uint),
    ('x', c_int),
    ('y', c_int),
    ('width', c_int),
    ('height', c_int),
    ('count', c_int),
]

GLXPbufferClobberEvent = struct_anon_96 	# /usr/include/GL/glx.h:343
class struct___GLXEvent(Union):
    __slots__ = [
        'glxpbufferclobber',
        'pad',
    ]
struct___GLXEvent._fields_ = [
    ('glxpbufferclobber', GLXPbufferClobberEvent),
    ('pad', c_long * 24),
]

GLXEvent = struct___GLXEvent 	# /usr/include/GL/glx.h:348
# GLXEXT_LEGACY (/usr/include/GL/glx.h:350)
# VERSION_1_3 (/usr/include/GL/glxext.h:59)
# VERSION_1_4 (/usr/include/GL/glxext.h:118)
# ARB_get_proc_address (/usr/include/GL/glxext.h:123)
# ARB_multisample (/usr/include/GL/glxext.h:126)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:131)
# SGIS_multisample (/usr/include/GL/glxext.h:136)
# EXT_visual_info (/usr/include/GL/glxext.h:141)
# SGI_swap_control (/usr/include/GL/glxext.h:160)
# SGI_video_sync (/usr/include/GL/glxext.h:163)
# SGI_make_current_read (/usr/include/GL/glxext.h:166)
# SGIX_video_source (/usr/include/GL/glxext.h:169)
# EXT_visual_rating (/usr/include/GL/glxext.h:172)
# EXT_import_context (/usr/include/GL/glxext.h:179)
# SGIX_fbconfig (/usr/include/GL/glxext.h:185)
# SGIX_pbuffer (/usr/include/GL/glxext.h:199)
# SGI_cushion (/usr/include/GL/glxext.h:227)
# SGIX_video_resize (/usr/include/GL/glxext.h:230)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:235)
# SGIX_swap_group (/usr/include/GL/glxext.h:239)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:242)
# SGIS_blended_overlay (/usr/include/GL/glxext.h:245)
# SGIS_shared_multisample (/usr/include/GL/glxext.h:249)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:254)
# 3DFX_multisample (/usr/include/GL/glxext.h:257)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:262)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:265)
# MESA_release_buffers (/usr/include/GL/glxext.h:268)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:271)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:276)
# OML_swap_method (/usr/include/GL/glxext.h:280)
# OML_sync_control (/usr/include/GL/glxext.h:287)
# NV_float_buffer (/usr/include/GL/glxext.h:290)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:294)
# MESA_agp_offset (/usr/include/GL/glxext.h:307)
# ARB_get_proc_address (/usr/include/GL/glxext.h:313)
# SGIX_video_source (/usr/include/GL/glxext.h:317)
# SGIX_fbconfig (/usr/include/GL/glxext.h:321)
# SGIX_pbuffer (/usr/include/GL/glxext.h:326)
# VERSION_1_3 (/usr/include/GL/glxext.h:358)
# VERSION_1_4 (/usr/include/GL/glxext.h:400)
# ARB_get_proc_address (/usr/include/GL/glxext.h:408)
# ARB_multisample (/usr/include/GL/glxext.h:416)
# ARB_fbconfig_float (/usr/include/GL/glxext.h:420)
# SGIS_multisample (/usr/include/GL/glxext.h:424)
# EXT_visual_info (/usr/include/GL/glxext.h:428)
# SGI_swap_control (/usr/include/GL/glxext.h:432)
# SGI_video_sync (/usr/include/GL/glxext.h:440)
# SGI_make_current_read (/usr/include/GL/glxext.h:450)
# SGIX_video_source (/usr/include/GL/glxext.h:460)
# EXT_visual_rating (/usr/include/GL/glxext.h:472)
# EXT_import_context (/usr/include/GL/glxext.h:476)
# SGIX_fbconfig (/usr/include/GL/glxext.h:492)
# SGIX_pbuffer (/usr/include/GL/glxext.h:510)
# SGI_cushion (/usr/include/GL/glxext.h:526)
# SGIX_video_resize (/usr/include/GL/glxext.h:534)
# SGIX_dmbuffer (/usr/include/GL/glxext.h:550)
# SGIX_swap_group (/usr/include/GL/glxext.h:560)
# SGIX_swap_barrier (/usr/include/GL/glxext.h:568)
# SUN_get_transparent_index (/usr/include/GL/glxext.h:578)
# MESA_copy_sub_buffer (/usr/include/GL/glxext.h:586)
# MESA_pixmap_colormap (/usr/include/GL/glxext.h:594)
# MESA_release_buffers (/usr/include/GL/glxext.h:602)
# MESA_set_3dfx_mode (/usr/include/GL/glxext.h:610)
# SGIX_visual_select_group (/usr/include/GL/glxext.h:618)
# OML_swap_method (/usr/include/GL/glxext.h:622)
# OML_sync_control (/usr/include/GL/glxext.h:626)
# NV_float_buffer (/usr/include/GL/glxext.h:642)
# SGIX_hyperpipe (/usr/include/GL/glxext.h:646)
# MESA_agp_offset (/usr/include/GL/glxext.h:693)

__all__ = ['GLX_USE_GL', 'GLX_BUFFER_SIZE', 'GLX_LEVEL', 'GLX_RGBA',
'GLX_DOUBLEBUFFER', 'GLX_STEREO', 'GLX_AUX_BUFFERS', 'GLX_RED_SIZE',
'GLX_GREEN_SIZE', 'GLX_BLUE_SIZE', 'GLX_ALPHA_SIZE', 'GLX_DEPTH_SIZE',
'GLX_STENCIL_SIZE', 'GLX_ACCUM_RED_SIZE', 'GLX_ACCUM_GREEN_SIZE',
'GLX_ACCUM_BLUE_SIZE', 'GLX_ACCUM_ALPHA_SIZE', 'GLX_BAD_SCREEN',
'GLX_BAD_ATTRIBUTE', 'GLX_NO_EXTENSION', 'GLX_BAD_VISUAL', 'GLX_BAD_CONTEXT',
'GLX_BAD_VALUE', 'GLX_BAD_ENUM', 'GLX_VENDOR', 'GLX_VERSION',
'GLX_EXTENSIONS', 'GLX_WINDOW_BIT', 'GLX_PIXMAP_BIT', 'GLX_PBUFFER_BIT',
'GLX_RGBA_BIT', 'GLX_COLOR_INDEX_BIT', 'GLX_PBUFFER_CLOBBER_MASK',
'GLX_FRONT_LEFT_BUFFER_BIT', 'GLX_FRONT_RIGHT_BUFFER_BIT',
'GLX_BACK_LEFT_BUFFER_BIT', 'GLX_BACK_RIGHT_BUFFER_BIT',
'GLX_AUX_BUFFERS_BIT', 'GLX_DEPTH_BUFFER_BIT', 'GLX_STENCIL_BUFFER_BIT',
'GLX_ACCUM_BUFFER_BIT', 'GLX_CONFIG_CAVEAT', 'GLX_X_VISUAL_TYPE',
'GLX_TRANSPARENT_TYPE', 'GLX_TRANSPARENT_INDEX_VALUE',
'GLX_TRANSPARENT_RED_VALUE', 'GLX_TRANSPARENT_GREEN_VALUE',
'GLX_TRANSPARENT_BLUE_VALUE', 'GLX_TRANSPARENT_ALPHA_VALUE', 'GLX_DONT_CARE',
'GLX_NONE', 'GLX_SLOW_CONFIG', 'GLX_TRUE_COLOR', 'GLX_DIRECT_COLOR',
'GLX_PSEUDO_COLOR', 'GLX_STATIC_COLOR', 'GLX_GRAY_SCALE', 'GLX_STATIC_GRAY',
'GLX_TRANSPARENT_RGB', 'GLX_TRANSPARENT_INDEX', 'GLX_VISUAL_ID', 'GLX_SCREEN',
'GLX_NON_CONFORMANT_CONFIG', 'GLX_DRAWABLE_TYPE', 'GLX_RENDER_TYPE',
'GLX_X_RENDERABLE', 'GLX_FBCONFIG_ID', 'GLX_RGBA_TYPE',
'GLX_COLOR_INDEX_TYPE', 'GLX_MAX_PBUFFER_WIDTH', 'GLX_MAX_PBUFFER_HEIGHT',
'GLX_MAX_PBUFFER_PIXELS', 'GLX_PRESERVED_CONTENTS', 'GLX_LARGEST_PBUFFER',
'GLX_WIDTH', 'GLX_HEIGHT', 'GLX_EVENT_MASK', 'GLX_DAMAGED', 'GLX_SAVED',
'GLX_WINDOW', 'GLX_PBUFFER', 'GLX_PBUFFER_HEIGHT', 'GLX_PBUFFER_WIDTH',
'GLX_SAMPLE_BUFFERS', 'GLX_SAMPLES', '__GLXextFuncPtr', 'GLXContextID',
'GLXPixmap', 'GLXDrawable', 'GLXPbuffer', 'GLXPbufferSGIX', 'GLXWindow',
'GLXFBConfigID', 'GLXContext', 'GLXFBConfig', 'glXChooseVisual',
'glXCopyContext', 'glXCreateContext', 'glXCreateGLXPixmap',
'glXDestroyContext', 'glXDestroyGLXPixmap', 'glXGetConfig',
'glXGetCurrentContext', 'glXGetCurrentDrawable', 'glXIsDirect',
'glXMakeCurrent', 'glXQueryExtension', 'glXQueryVersion', 'glXSwapBuffers',
'glXUseXFont', 'glXWaitGL', 'glXWaitX', 'GLX_VERSION_1_1',
'glXGetClientString', 'glXQueryServerString', 'glXQueryExtensionsString',
'GLX_VERSION_1_2', 'glXGetCurrentDisplay', 'GLX_VERSION_1_3',
'glXChooseFBConfig', 'glXCreateNewContext', 'glXCreatePbuffer',
'glXCreatePixmap', 'glXCreateWindow', 'glXDestroyPbuffer', 'glXDestroyPixmap',
'glXDestroyWindow', 'glXGetCurrentReadDrawable', 'glXGetFBConfigAttrib',
'glXGetFBConfigs', 'glXGetSelectedEvent', 'glXGetVisualFromFBConfig',
'glXMakeContextCurrent', 'glXQueryContext', 'glXQueryDrawable',
'glXSelectEvent', 'PFNGLXGETFBCONFIGSPROC', 'PFNGLXCHOOSEFBCONFIGPROC',
'PFNGLXGETFBCONFIGATTRIBPROC', 'PFNGLXGETVISUALFROMFBCONFIGPROC',
'PFNGLXCREATEWINDOWPROC', 'PFNGLXDESTROYWINDOWPROC', 'PFNGLXCREATEPIXMAPPROC',
'PFNGLXDESTROYPIXMAPPROC', 'PFNGLXCREATEPBUFFERPROC',
'PFNGLXDESTROYPBUFFERPROC', 'PFNGLXQUERYDRAWABLEPROC',
'PFNGLXCREATENEWCONTEXTPROC', 'PFNGLXMAKECONTEXTCURRENTPROC',
'PFNGLXGETCURRENTREADDRAWABLEPROC', 'PFNGLXGETCURRENTDISPLAYPROC',
'PFNGLXQUERYCONTEXTPROC', 'PFNGLXSELECTEVENTPROC',
'PFNGLXGETSELECTEDEVENTPROC', 'GLX_VERSION_1_4', 'glXGetProcAddress',
'PFNGLXGETPROCADDRESSPROC', 'GLX_ARB_get_proc_address',
'glXGetProcAddressARB', 'PFNGLXGETPROCADDRESSARBPROC',
'GLXPbufferClobberEvent', 'GLXEvent']
# END GENERATED CONTENT (do not edit above this line)

# From glxproto.h
GLXBadContext = 0
GLXBadContextState = 1
GLXBadDrawable = 2
GLXBadPixmap = 3
GLXBadContextTag = 4
GLXBadCurrentWindow = 5
GLXBadRenderRequest = 6
GLXBadLargeRequest = 7
GLXUnsupportedPrivateRequest = 8
GLXBadFBConfig = 9
GLXBadPbuffer = 10
GLXBadCurrentDrawable = 11
GLXBadWindow = 12

__all__ += ['GLXBadContext', 'GLXBadContextState', 'GLXBadDrawable',
'GLXBadPixmap', 'GLXBadContextTag', 'GLXBadCurrentWindow',
'GLXBadRenderRequest', 'GLXBadLargeRequest', 'GLXUnsupportedPrivateRequest',
'GLXBadFBConfig', 'GLXBadPbuffer', 'GLXBadCurrentDrawable', 'GLXBadWindow']



