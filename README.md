`IN THE NAME OF GOD`

# Fekre Bekr

### `FekreBekr` is Really Fun Puzzle Guessing Game.

---

#### Running:

For Execute This Code Need Python Version `3.10` Or Newer .

**Run In Older Version**

If Want Run In Older Python Version Must Be Change `match`  statement `(line 116)` to `if` statement in `status` function `(line 93)` and Good To Go .

**Run Game**

After Download Code Execute `main.py` 

This Line Run Game

```shell
python main.py
```

After Hit Enter Game Is Runiing & Wait For First Guess

```shell
LEVEL < 1 >
LVL <1> - CHAR [5]
GUESS [6]/[6] />: 
```

Change Some Options

```shell
python main.py --length 6 --guess 10
```

And This Changed

```shell
LEVEL < 1 >
LVL <1> - CHAR [6]
GUESS [10]/[10] />: 
```



See Run Options

**Exit**

For Exit Any Time From Game Need Only  type `exit` in Input 

```shell
LEVEL < 1 >
LVL <1> - CHAR [5]
GUESS [6]/[6] />: exit
```

After Exiting Or Game Over Game Create or Overwrite `detail.json` or path Define 

See Run Options

---

#### 

#### Detail:

Detail File Created With Json Pattern . `detail.json`

`KEY` is Level Target

> **Level Detail**
> 
> > `level :` *Level Number* - `int`
> > 
> > `guesses :` *Guess Counter* - `int`
> > 
> > `record :` *Record All Guesses With State Analyze* - `dict`

> **Record Mean** 
> 
> > `0 :` *Wrong Value*
> > 
> > `1 :` *True Value & True Sit*
> > 
> > `2 :` *True Value But Wrong Sit*

---



#### Run Options:

> **Run Options**
> 
> > `--length :` *Length Of Target For Starting Game* - `deafult = 5`
> > 
> > `--guess :` *Guess Limit* - `default = 6`
> > 
> > `--detail :` *Path For Save Detail* - `deafult = './detail.json'`

---
