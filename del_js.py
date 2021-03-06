#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_js_code():
    js_code = """
    (function() {
        'use strict';
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })

        function fakeActiveVRDisplays() { return "Not Spoofed"; }
        function fakeAppCodeName() {
          return "Mozilla";
        }
        function fakeAppName() {
          return "Netscape";
        }

        function fakeAppVersion() {
            return "5.0 (Windows)";
        }
        function fakeBattery() { return "Not Spoofed"; }
        function fakeConnection() { return window.navigator.connection; }
        function fakeGeoLocation() { return "Not Spoofed"; }
        function fakeHardwareConcurrency() {
          return 1;//hardware [1,2,4,6,8,12,16,32]
        }
        function fakeJavaEnabled() {
          return true;
        }
        function fakeLanguage() {
            // NOTE: TOR Browser uses American English
            return "en-US";
        }
        function fakeLanguages() {
            // NOTE: TOR Browser uses American English
            return "en-US,en";
        }
        function fakeMimeTypes() { return window.navigator.mimeTypes; }
        function fakeOnLine() {
          return true;
        }
        function fakeOscpu() {
          return "Windows NT 5.0";
        }
        function fakePermissions() { return "Not Spoofed"; }
        function fakePlatform() {
          return "Win64";
        }
        function fakePlugins() {
            return window.navigator.plugins;
        }
        function fakeProduct() {
          return "Gecko";
        }
        function fakeServiceWorker() { return window.navigator.serviceWorker; }
        function fakeStorage() { return "Not Spoofed"; }
        function fakeUserAgent() {
            return "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36";
        }
        function fakeBuildID() {
          return "20100101";
        }

        const fakeActiveVRDisplaysValue       = fakeActiveVRDisplays();
        const fakeAppCodeNameValue            = fakeAppCodeName();
        const fakeAppNameValue                = fakeAppName();
        const fakeAppVersionValue             = fakeAppVersion();
        const fakeBatteryValue                = fakeBattery();
        const fakeConnectionValue             = fakeConnection();
        const fakeGeoLocationValue            = fakeGeoLocation();
        const fakeHardwareConcurrencyValue    = fakeHardwareConcurrency();
        const fakeJavaEnabledValue            = fakeJavaEnabled();
        const fakeLanguageValue               = fakeLanguage();
        const fakeLanguagesValue              = fakeLanguages();
        const fakeMimeTypesValue              = fakeMimeTypes();
        const fakeOnLineValue                 = fakeOnLine();
        const fakeOscpuValue                  = fakeOscpu();
        const fakePermissionsValue            = fakePermissions();
        const fakePlatformValue               = fakePlatform();
        const fakePluginsValue                = fakePlugins();
        const fakeProductValue                = fakeProduct();
        const fakeServiceWorkerValue          = fakeServiceWorker();
        const fakeStorageValue                = fakeStorage();
        const fakeUserAgentValue              = fakeUserAgent();
        const fakeBuildIDValue                = fakeBuildID();

        Object.defineProperties(window.navigator, {
            activeVRDisplays: {
                configurable: true,
                enumerable: true,
                get: function getActiveVRDisplays() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.activeVRDisplays");
                    return fakeActiveVRDisplaysValue;
                }
            },

            
            appCodeName: {
                configurable: true,
                enumerable: true,
                get: function getAppCodeName() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.appCodeName");

                    return fakeAppCodeNameValue;
                }
            },
            appName: {
                configurable: true,
                enumerable: true,
                get: function getAppName() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.appName");

                    return fakeAppNameValue;
                }
            },
            appVersion: {
                configurable: true,
                enumerable: true,
                get: function getAppVersion() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.appVersion");

                    return fakeAppVersionValue;
                }
            },

            // TODO: This is getBattery() now

            battery: {
                configurable: true,
                enumerable: true,
                get: function getBattery() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.battery");
                    return fakeBatteryValue;
                }
            },  
            connection: {
                configurable: true,
                enumerable: true,
                get: function getConnection() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.connection");
                    return fakeConnectionValue;
                }
            },
            geolocation: {
                configurable: true,
                enumerable: true,
                get: function getGeoLocation() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.geolocation");
                    return fakeGeoLocationValue;
                }
            },

            hardwareConcurrency: {
                configurable: true,
                enumerable: true,
                get: function getHardwareConcurrency() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.hardwareConcurrency");

                    return fakeHardwareConcurrencyValue;
                }
            },

            javaEnabled: {
                configurable: true,
                enumerable: true,
                value: function getJavaEnabled() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.javaEnabled");
                    return fakeJavaEnabledValue;
                }
            },

            language: {
                configurable: true,
                enumerable: true,
                get: function getLanguage() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.language");

                    return fakeLanguageValue;
                }
            },
            languages: {
                configurable: true,
                enumerable: true,
                get: function getLanguages() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.languages");

                    return fakeLanguagesValue;
                }
            },

            mimeTypes: {
                configurable: true,
                enumerable: true,
                get: function getMimeTypes() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.mimeTypes");
                    return fakeMimeTypesValue;
                }
            },

            onLine: {
                configurable: true,
                enumerable: true,
                get: function getOnLine() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.onLine");

                    return fakeOnLineValue;
                }
            },
            oscpu: {
                configurable: true,
                enumerable: true,
                get: function getOscpu() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.oscpu");

                    return fakeOscpuValue;
                }
            },

            permissions: {
                configurable: true,
                enumerable: true,
                get: function getPermissions() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.permissions");
                    return fakePermissionsValue;
                }
            },

            platform: {
                configurable: true,
                enumerable: true,
                get: function getPlatform() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.platform");

                    return fakePlatformValue;
                }
            },

            plugins: {
                configurable: true,
                enumerable: true,
                get: function getPlugins() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.plugins");
                    return fakePluginsValue;
                }
            },

            product: {
                configurable: true,
                enumerable: true,
                get: function getProduct() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.product");

                    return fakeProductValue;
                }
            },

            serviceWorker: {
                configurable: true,
                enumerable: true,
                get: function getServiceWorker() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.serviceWorker");
                    return fakeServiceWorkerValue;
                }
            },
            storage: {
                configurable: true,
                enumerable: true,
                get: function getStorage() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.storage");
                    return fakeStorageValue;
                }
            },
            userAgent: {
                configurable: true,
                enumerable: true,
                get: function getUserAgent() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.userAgent");

                    return fakeUserAgentValue;
                }
            },
            /*buildID: {
                configurable: true,
                enumerable: true,
                get: function getBuildID() {
                    console.log("[ALERT] " + window.location.hostname + " accessed property Navigator.buildID");

                    return fakeBuildIDValue;
                }
            }*/
        });
    })();
    """

    return js_code


if __name__ == '__main__':
    res = get_js_code()
    print(res)
