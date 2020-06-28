import os
import shutil


def make_doc():
    """Run Sphinx to build the doc."""
    try:
        # removing previous build
        print('removing previous build')
        command_line_string = 'make clean'
        os.system(command_line_string)
        shutil.rmtree('../docs/', ignore_errors=True)

        # new build
        command_line_string = 'make html'
        os.system(command_line_string)

        # copy files
        print('copy files')
        command_line_string = r'xcopy _build\html\. ..\docs\ /e /Y /q'
        os.system(command_line_string)

        command_line_string = r'xcopy .nojekyll ..\docs'
        os.system(command_line_string)

    except Exception as error:
        print(error)


if __name__ == '__main__':
    make_doc()
