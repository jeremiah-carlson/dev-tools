# Contents

# Snippets

## Setup

### Read Configs
```python
def parse_configs()-> Dict:
    with open(PARENT_DIR / 'conf' / 'config.yaml', 'r') as conf:
        return yaml.safe_load(conf)
```


## Data Formatting

### Format Headers
```python
def working_headers(data:pd.DataFrame):
    return data.rename(columns=dict(zip(data.columns,[x.lower().replace(' ', '_') for x in data.columns])))

def camel_headers(data:pd.DataFrame):
    cnames = [re.sub(r'(_|-)+', ' ', x).title().replace(' ', '') for x in data.columns]
    cnames = [''.join([x[0].lower(), x[1:]]) for x in cnames]
    return data.rename(columns=dict(zip(data.columns,cnames)))

def presentation_headers(data:pd.DataFrame):
    return data.rename(columns=dict(zip(data.columns,[x.title().replace('_', ' ') for x in data.columns])))
```

## Logging
### Basic Log
```python
class log():
    def __init__(self, line:list, title='', sep='\t', path=''):
        if title == '':
            self.title = 'log.txt'
        else:
            self.title = title + '_log.txt'
        self.line = line
        self.sep = sep
        self.path = path

    def write_log(self):
        with open(self.path + self.title, 'a+') as lg:
            lg.write(self.sep.join(self.line) + '\n')
```

### Log Runtime Data
```python
def log_runtime()-> None:
    with open(PARENT_DIR / 'conf' / 'runtime.yaml', 'w') as p_log:
        p_log.write('ppid: %s\npid: %s' % (os.getppid(), os.getpid()))
```