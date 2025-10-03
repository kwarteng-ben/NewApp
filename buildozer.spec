[app]
title = QuotesApp  # App name shown on device
package.name = quotesapp  # Unique package name
package.domain = org.example  # Your domain

source.dir = .  # Current directory
source.include_exts = py,png,jpg,kv,atlas  # File extensions to include

version = 0.1  # App version
requirements = python3,kivy  # Dependencies (your code only needs these)

orientation = portrait  # Lock to portrait mode if desired

[buildozer]
log_level = 2  # Verbose logging for debugging

[android]
android.api = 34  # Target Android API level
android.minapi = 21  # Minimum supported Android version
android.ndk = 25b  # NDK version
android.sdk = 34  # SDK version
android.build_tools = 34.0.0  # Build-tools version (stable, avoids your 36.1 error)
android.accept_sdk_license = True  # Automatically accept licenses (fixes your error)

android.gradle_dependencies = 

android.enable_androidx = True
android.meta_data = 
    android:name="io.kivy.android.bootstrap"
    android:value="SDL2"

android.add_src = 

android.add_aar = 

android.add_gradle = 

android.gradle_dependencies = 

android.enable_androidx = True

android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"
