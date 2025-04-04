import configparser


class ConfigHandler:
    file_path = "config.ini"

    @staticmethod
    def save_to_config(section, key, value):
        config = configparser.ConfigParser()

        # Read the existing config file if it exists
        config.read(ConfigHandler.file_path)

        # Add a new section if it doesn't exist
        if section not in config:
            config[section] = {}

        # Add or update the key-value pair
        config[section][key] = value

        # Write the changes back to the file
        with open(ConfigHandler.file_path, "w") as configfile:
            config.write(configfile)

    def read_from_config(section, key):
        config = configparser.ConfigParser()
        config.read(ConfigHandler.file_path)

        if section in config and key in config[section]:
            return config[section][key]
        else:
            return None
