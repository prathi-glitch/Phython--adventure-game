
[app]
android.accept_sdk_license = True

title = Python Adventure
package.name = pythonadventure
package.domain = org.prathi

source.dir = .
source.include_exts = py,kv,png,jpg,txt

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23
android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
