# MEDomicsTools Good Practices

This document presents the good practices to use for various deep learning applications.

## Table of Contents

NOTES: 

- To update the Table of Contents, use: https://ecotrust-canada.github.io/markdown-toc/
- Section headers cannot contain special characters other than -, otherwise the TOC hyperlinks will not work

## Contributors

- [Simon Giard-Leroux](https://github.com/sgiardl)

## Changelog

Revision | Date       | Description |
---------| -----------| ----------- |
A        | 2022-04-28 | Creation    |

## To-Do

- [ ] Learning rate warmup
- [ ] 

## Good Practices

### Learning Rate Warmup

A warmup period can be used at the start of training for a few epochs before reaching the peak learning rate.

See the following paper for details: [On the adequacy of untuned warmup for adaptive optimization](https://arxiv.org/abs/1910.04209)

The following is an example of implementation in PyTorch:

```python
def __build_scheduler(
    self,
    n_warmup: int,
    n_epochs: int,
    warmup_floor: float = 0.1,
    decay_floor: float = 0.1,
) -> Any:
    """Method to build the scheduler for training.
    Args:
        n_warmup (int): number of warmup epochs
        n_epochs (int): number of total epochs
        warmup_floor (float, optional): learning rate ratio when starting the warmup phase. Defaults to 0.1.
        decay_floor (float, optional): learning rate ratio when decaying during the decay phase. Defaults to 0.1.
    Returns:
        any: scheduler
    """
    # Sets a warmup period for the learning rate
    # https://arxiv.org/pdf/1910.04209.pdf
    warmup_scheduler = LinearLR(
        optimizer=self.__optimizer,
        start_factor=warmup_floor,
        end_factor=1.0,
        total_iters=n_warmup,
    )

    # Reduces the learning rate after warmup period
    decay_scheduler = CosineAnnealingLR(
        optimizer=self.__optimizer,
        T_max=n_epochs - n_warmup,
        eta_min=self.__learning_rate * decay_floor,
    )

    # Creating the scheduler
    return SequentialLR(
        optimizer=self.__optimizer,
        schedulers=[warmup_scheduler, decay_scheduler],
        milestones=[n_warmup + 1],
    )

```

