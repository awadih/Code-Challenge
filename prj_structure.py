import os


def list_files(start_path, file_name):
    content = ''
    for root, dirs, files in os.walk(start_path):
        if os.path.basename(root) != '.idea':
            level = root.replace(start_path, '').count(os.sep)
            indent = ' ' * 4 * level
            content += '{}{}/\n'.format(indent, os.path.basename(root))
            print('{}{}/'.format(indent, os.path.basename(root)))
            sub_indent = ' ' * 4 * (level + 1) + '|' + '--'
            for f in files:
                print('{}{}'.format(sub_indent, f))
                content += '{}{}\n'.format(sub_indent, f)
    with open(start_path + '/' + file_name, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    list_files('./..', 'prj_structure.txt')
