'''OpenGL extension EXT.packed_depth_stencil

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_packed_depth_stencil'
_DEPRECATED = False
GL_DEPTH_STENCIL_EXT = constant.Constant( 'GL_DEPTH_STENCIL_EXT', 0x84F9 )
GL_UNSIGNED_INT_24_8_EXT = constant.Constant( 'GL_UNSIGNED_INT_24_8_EXT', 0x84FA )
GL_DEPTH24_STENCIL8_EXT = constant.Constant( 'GL_DEPTH24_STENCIL8_EXT', 0x88F0 )
GL_TEXTURE_STENCIL_SIZE_EXT = constant.Constant( 'GL_TEXTURE_STENCIL_SIZE_EXT', 0x88F1 )


def glInitPackedDepthStencilEXT():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )
