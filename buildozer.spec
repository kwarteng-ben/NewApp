[app]
title = QuotesApp
package.name = quotesapp
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[android]
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34
android.build_tools = 34.0.0
android.accept_sdk_license = True

android.enable_androidx = True
android.meta_data = 
    android:name="io.kivy.android.bootstrap"
    android:value="SDL2"

android.add_src = 

android.add_aar = 

android.add_gradle = 

android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"

[android.deploy]
dist_name = quotesapp.apk
