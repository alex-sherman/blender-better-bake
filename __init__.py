# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
import better_bake

if "bpy" in locals():
    import importlib
    if "better_bake" in locals():
        importlib.reload(better_bake.anim)

import bpy
from better_bake.anim import BetterBakeAction

bl_info = {
    "name": "Better Action Baking",
    "author": "Alex Sherman",
    "version": (0, 1, 0),
    "blender": (2, 76, 0),
    "description": "Bake actions ignoring locked transforms",
    #"tracker_url": "",
    #"wiki_url": "",
    "category": "Action"}

try:
    import pydevd
    pydevd.settrace(stdoutToServer=True, stderrToServer=True, suspend=False)
except ImportError:
    pass


class Mesh(object):

    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return '<Mesh(%s)>' % self.s


def menu_func(self, context):
    self.layout.operator(BetterBakeAction.bl_idname, text="Better Action Baking")


def register():
    print(BetterBakeAction.bl_idname)
    bpy.utils.register_class(BetterBakeAction)
    bpy.types.INFO_MT_file_export.append(menu_func)


def unregister():
    bpy.utils.unregister_class(BetterBakeAction)
    bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    register()
