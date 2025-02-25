import ctypes

import wx
from wx.glcanvas import GLCanvas, GLContext
from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT, glGetString, GL_VERSION
import OpenGL.GL as gl

libjewel = ctypes.CDLL("../libjewel/cmake-build-debug/libjewel.dylib")
libjewel.draw_triangle.argtypes = []
libjewel.draw_triangle.restype = None # Ensure the return type is void

class JewelCanvas(GLCanvas):

    def __init__(self, parent):
        super().__init__(parent)
        self.context = GLContext(self)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_SIZE, self.on_size)  # Handle window resizing
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.on_erase_background)  # Prevent flickering

    def on_erase_background(self, event):
        """Prevent flickering on macOS."""
        pass  # Do nothing

    def on_size(self, event):
        """Handle resizing to prevent OpenGL errors."""
        if self.IsShownOnScreen():
            self.SetCurrent(self.context)
        event.Skip()  # Allow default resizing behavior


    def on_paint(self, event):
        """Handle OpenGL rendering."""
        if not self.IsShownOnScreen():  # Ensure window is visible
            return

        self.SetCurrent(self.context)

        try:
            # Ensure OpenGL context is valid before calling OpenGL functions
            version = glGetString(GL_VERSION)
            if version is None:
                print("⚠️ OpenGL context lost! Skipping draw.")
                return  # Skip drawing if context is lost

            glClear(GL_COLOR_BUFFER_BIT)

            libjewel.draw_triangle()  # Call the C function

            self.SwapBuffers()

        except gl.GLError as e:
            print(f"⚠️ OpenGL Error: {e}")  # Log errors but don't crash the app
