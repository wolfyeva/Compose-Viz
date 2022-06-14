# Final Project Report- Team 14(compose-viz)
###### tags: `software-testing`

## Group Members
| Name   | E-mail                   | Student ID |
| ------ | ------------------------ |:---------- |
| 吳星翰 | xyphuzwu@gmail.com       | B102573    |
| 歐陽詮 | charlie890414@gmail.com  | B102523    |
| 林奕宏 | justin89721@g.ncu.edu.tw | B102534    |
| 王均琦 | evawang12@g.ncu.edu.tw   | B102527    |
| 施泓丞 | ant5646@g.ncu.edu.tw     | B102524    |

## About compose-viz (TDD)
![](https://camo.githubusercontent.com/bb73761c43348432c6e6f55c310f91b84a036fd980e89408c2d848a150b615a6/68747470733a2f2f736f6369616c6966792e6769742e63692f636f6d706f73652d76697a2f636f6d706f73652d76697a2f696d6167653f6465736372697074696f6e3d3126666f6e743d4b6f486f266e616d653d31266f776e65723d31267061747465726e3d43697263756974253230426f617264267468656d653d4c69676874)
## Source Code (GitHub)
[GitHub Repository](https://github.com/compose-viz/compose-viz.git)

## The Discussion
[On HackMD](https://hackmd.io/@wst24365888/Hy15z_1z5) (Once a week)

## Teams recording URLs
We have our regular meeting on Google Meet.
Recording Link: [on Youtube](https://youtu.be/9X6nd51OBrs)



## Testing Results Listing
### Overview
- 43 Test Cases
    - According to [The Compose Specification](https://github.com/compose-spec/compose-spec/blob/master/spec.md)
- 100% Code Coverage
- 13 Visualization Components
- 67(422) Assertions

### E2E
- From cil to graph output

### Intergation Test
- cil -> parser
- Inside parser
- Parser output -> graph generator

### Continuous Integration
- Github Actions
    - Test
        - When push or PR on branch main & dev
    - Github Release
        - On every push of tag: v*
    - Publish to PyPi
        - On every push of tag: v*

### Pre-commit
pre-commit hooks:
- flake8: linter
- isort: sort import dependencies
- black: formatter
- pyright: static type checker




