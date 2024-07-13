plugins {
    id("java")
    id("application")
}

group = "tld.coursera"
version = "1.0"

repositories {

    mavenCentral()
    flatDir {
        dirs("lib")
    }
}


dependencies {
    implementation("LocalLibrary","algs4")
}