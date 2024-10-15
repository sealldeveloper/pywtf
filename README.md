# PyWTF `a-z()+`

PyWTF is an esoteric and educational programming style based on JSFuck and inspired by [this tweet](https://x.com/chordbug/status/1834642829919781369). It uses only built-in functions to execute code.

It does not depend on a browser, so you can even run it with Python (to come).

Demo: https://pywtf.seall.dev

By [@sealldev](https://twitter.com/sealldev) and [friends](https://github.com/sealldeveloper/pywtf/graphs/contributors).

### Example

The following source will do an `print(1)`:

```python
exec(chr(ord(str(int(not())+int(not())))+ord(next(reversed(str(object())))))+
next(iter(str(range(not()))))+chr(ord(str(int()))+ord(next(reversed(hex(ord(
max(str(bytearray()))))))))+chr(int(str(int(not()))+str(int(not()))+str(int()
)))+max(str(set()))+min(str(set()))+str(int(not()))+next(reversed(str(range(
not())))))
```

### Basics

    True        =>  not()
    False       =>  ()in()
    None        =>  str(set().add(()))
    0           =>  int()
    1           =>  (not())
    2           =>  (not())+(not())
    10          =>  int(str(+(not()))+str(int()))
    a           =>  chr(max(range(ord(max(bin(int()))))))
    <num>+1     =>  <num>+(not())
    <num>-1      =>  max(range(<num>))

See the full list at a later date...  

# How it Works

Todo

# Further Readings

Todo
