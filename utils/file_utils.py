class FileUtils:
    @staticmethod
    def replace_file(file, old_str, new_str, encoding: str = 'utf-8'):
        """
        param file: 文件名
        param old_str: 旧字符串
        param new_str: 新字符串
        """
        file_data = ""
        with open(file, 'r', encoding = encoding) as f:
            for line in f:
                if old_str in line:
                    line = line.replace(old_str, new_str)
                file_data += line
        with open(file, 'w', encoding = encoding) as f:
            f.write(file_data)