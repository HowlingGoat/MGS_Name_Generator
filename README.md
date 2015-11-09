# MGS_Name_Generator
## General Use
MGS name generator is a python script that tries to randomly creates MGS staff names. Note that all first and second names might not be present.
Tested on GNU/Linux with Python 2.7.10.

To run, use `./metal_name_generator.py [options]` or `python metal_name_generator.py [options]`, you may need to make the
script executable with `chmod +x metal_name_geneartor.py`.

Several options are available:

  * `-h` is for the built in help.
  * `-e` for a larger than usual list of first and second names.
  * `-n #` to create more than one name at the time, where `#` is the number of names to be generated.
  * `-f [files.ext]` is one or more files to add first names to the generation process. Each name should be on a single line.
  * `-l [files.ext]` is one or more files to add last names to the generation process. Each name should be on a single line.
  * `-s "sep"` is the separator to be used instead of a whitespace, where `sep` is what will be used. The quotes are not absolutely necessary but will help make sure the script gets the correct value. For example, you might use `-s "_"` to have the first and last name separated by an underscore.

## Module use
MGS name generator could be used as a module to return the generated names in a list.
The main fucntion to use is `main(count, seperator, extended)`. `count` (int) will change how much names are generated,
 `seperator` ("string") will decide how spaces are returned and `extended` (boolean) will decide if the extended lists are used.

To add files to the extended list, see the `first_files` and `last_files` lists. Each file added after the first one will be added when `extended=True`.

To use:

    import metal_name_generator

    names_list = metal_name_generator.main(1, " ", True)
    print names_list[0]
    >> Punching Hog

This example will first import the script, then generate a single name with a space as a seperator and the extended names.