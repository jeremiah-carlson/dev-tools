# Contents

# Snippets

# Accessability

## Key Binding

### Function On Key Press (Enter)

```javascript
function keyPressEnter(e, myFunc, args) {
    if (e.keyCode == 13) {
        myFunc(args);
    }
}
```