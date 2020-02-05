import os
import sys
import fnmatch
import shutil

class Packrat():

    def __init__(self, proj_dir):
        self.proj_dir = proj_dir
        if not os.path.isdir(self.proj_dir):
            sys.exit("'" + self.proj_dir + "' not found.")

        self.packrat_dir = os.path.normpath(self.proj_dir + "/packrat")

        if not os.path.isdir(self.packrat_dir):
            sys.exit("No packrat directory found in '" + self.proj_dir + "'.")
            
        self.libs = [os.path.normpath(self.packrat_dir + "/" + e)
                    for e in fnmatch.filter(os.listdir(self.packrat_dir),
                    "lib*"
                )
            ]

    def ln_lib(self, ln_source, verbose):
        """Link libraries to another location."""

        if not os.path.isdir(ln_source):
            sys.exit("'" + ln_source + "' not found.")

        source_libs = [os.path.normpath(ln_source + "/" + e)
                    for e in fnmatch.filter(os.listdir(ln_source),
                    "lib*"
                )
            ]

        for e in [os.path.normpath(self.packrat_dir + "/" + os.path.basename(e0)) for e0 in source_libs]:

            if os.path.exists(e) and (os.path.islink(e) or not os.path.isdir(e)):
                os.remove(e)
            elif os.path.exists(e):
                shutil.rmtree(e)
            if verbose == True:
                print("Removed: '" + e + "'.")
            os.symlink(
                os.path.normpath(
                    ln_source + "/" + os.path.basename(e)
                ),
            e)
            if verbose == True:
                print("Created symlink: '" + ln_source +
                    "/" + os.path.basename(e) +
                    "'.")
