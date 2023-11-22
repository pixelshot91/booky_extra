# From https://obsproject.com/wiki/Scripting-Tutorial-Source-Shake

import obspython as obs
import math, time

# Description displayed in the Scripts dialog window
def script_description():
  return """Source Shake!!
            Shake a source in the current scene when a hotkey is pressed. Go to Settings
             then Hotkeys to select the key combination.Check the
            Source Shake Scripting Tutorial on the OBS Wiki for more information."""

def script_tick(seconds):
  current_scene_as_source = obs.obs_frontend_get_current_scene()
  if current_scene_as_source:
    current_scene = obs.obs_scene_from_source(current_scene_as_source)
    scene_item = obs.obs_scene_find_source_recursive(current_scene, "barcode")
    if scene_item:
      obs.obs_sceneitem_set_rot(scene_item, 10*math.sin(2*time.time()))
    obs.obs_source_release(current_scene_as_source)
