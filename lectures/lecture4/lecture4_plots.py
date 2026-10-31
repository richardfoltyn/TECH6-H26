"""
Plotting functions for lecture 4.
"""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import logistic


def plot_true_relationship(f):
    """
    Plot the true relationship as a filled contour plot.

    Parameters
    ----------
    f : callable
        Function of the two features to plot.
    """
    # Create coordinates for x1 and x2
    x = np.linspace(0, 1, 50)
    x1_grid, x2_grid = np.meshgrid(x, x)

    # Deterministic function f(x1, x2)
    z = f(x1_grid, x2_grid)

    # Contour plot of deterministic function
    fig, ax = plt.subplots(figsize=(5.5, 4.5), layout='constrained')
    levels = np.linspace(-1, 1, 11)
    cntrf = ax.contourf(x1_grid, x2_grid, z, levels=levels, cmap='RdBu_r', alpha=0.7)
    CS = ax.contour(x1_grid, x2_grid, z, levels=levels, linewidths=0.5, colors='k')
    ax.clabel(CS, levels, fontsize=9)
    fig.colorbar(cntrf, ax=ax, shrink=0.6, label='f($x_1$, $x_2$)')
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')

    return ax


def plot_sigmoid():
    """
    Plot the sigmoid function (logistic CDF).
    """
    zvalues = np.linspace(-6, 6, 50)

    _, ax = plt.subplots(layout='constrained')
    ax.plot(zvalues, logistic.cdf(zvalues), lw=2.0)
    # Add horizontal and vertical lines
    for yvalue in (0.0, 0.5, 1.0):
        ax.axhline(yvalue, ls='--', lw=0.75, c='black')
    ax.axvline(0.0, ls='--', lw=0.75, c='black')
    ax.set_xlabel('$z$')
    ax.set_ylabel(r'$\sigma(z)$')
    ax.set_yticks([0.0, 0.5, 1.0])
    ax.set_title('Sigmoid function (logistic CDF)')

    return ax


def plot_classes(X, y):
    """
    Plot class labels for the given features.

    Parameters
    ----------
    X : array
        Features x1 and x2.
    y : array
        Binary class labels, 0 or 1.
    """
    fig, ax = plt.subplots(figsize=(4, 4))

    colors = ['steelblue', 'darkred']
    markers = ['o', '*']

    classes = np.unique(y)

    for i in classes:
        mask = y == i
        ax.scatter(
            X[mask, 0],
            X[mask, 1],
            s=50,
            marker=markers[i],
            c=colors[i],
            alpha=0.7,
            lw=0.75,
            label=f'Class {i}',
        )

    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    fig.legend(loc='upper left', ncols=1, bbox_to_anchor=(0.92, 0.89))

    return ax


def plot_decision_boundary(ax, x, classifier):
    """
    Plot the decision boundary of a classifier on a given Axes object.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes object to plot on.
    x : array-like
        Grid points for x1 and x2.
    classifier : object
        Fitted classifier used to predict class labels.

    """

    xx1, xx2 = np.meshgrid(x, x)

    X = np.column_stack((xx1.ravel(), xx2.ravel()))
    y_pred = classifier.predict(X)
    y_pred = y_pred.reshape(xx1.shape)

    colors = ['steelblue', 'darkred']
    cmap = ListedColormap(colors)

    # Fixed levels keep class colors consistent and draw one boundary between 0 and 1
    ax.contourf(
        xx1, xx2, y_pred, levels=[-0.5, 0.5, 1.5], cmap=cmap, alpha=0.15, zorder=-10
    )
    ax.contour(
        xx1, xx2, y_pred, levels=[0.5], colors='black', linewidths=0.5, zorder=-5
    )


def plot_accuracy_validation_curve(
    param_range,
    train_scores,
    test_scores,
    xlabel='Parameter C',
    log_scale=True,
    score='Accuracy',
    title=None,
):
    """
    Plot a validation curve with training and validation scores.

    Parameters
    ----------
    param_range : array-like
        Values of the hyperparameter.
    train_scores : array-like of shape (n_params, n_folds)
        Training scores for each parameter value and fold.
    test_scores : array-like of shape (n_params, n_folds)
        Validation scores for each parameter value and fold.
    xlabel : str
        Label for the horizontal axis.
    log_scale : bool
        Whether to use a logarithmic scale for the horizontal axis.
    score : str
        Metric name for the vertical axis and legend labels.
    title : str, optional
        Title for the plot.
    """

    # Compute average and standard deviation of scores across folds
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    train_label = f'Training {score}'
    validation_label = f'Validation {score}'

    plt.figure(figsize=(6, 4))
    plt.plot(param_range, train_mean, c='black', ls='--', label=train_label)
    plt.fill_between(
        param_range,
        train_mean + train_std,
        train_mean - train_std,
        alpha=0.15,
        color='black',
        lw=0,
    )
    plt.plot(
        param_range,
        test_mean,
        color='steelblue',
        lw=1.5,
        marker='o' if len(test_mean) < 20 else None,
        markersize=4,
        zorder=10,
        label=validation_label,
    )
    plt.fill_between(
        param_range,
        test_mean + test_std,
        test_mean - test_std,
        alpha=0.15,
        color='steelblue',
        lw=0,
    )
    if log_scale:
        plt.xscale('log')
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel(score)
    plt.title(title or 'Validation curve')

    ymin = min(np.amin(test_mean - test_std), np.amin(train_mean - train_std))
    ymin = np.floor(ymin * 10) / 10
    plt.ylim((ymin, 1.0))


def plot_generic_confusion_matrix():
    """
    Plot a generic confusion matrix.
    """

    # Artificial data
    data = np.array([[1, 0], [0, 1]])
    class_names = ['P', 'N']
    # Color map mapping 1 to green, 0 to red
    cm = ListedColormap(['#ffb7b5', '#93feb6'])
    # Square annotations
    ann = [
        'True positives (TP)',
        'False negatives (FN)',
        'False positives (FP)',
        'True negatives (TN)',
    ]
    ann = ['\n'.join(s.split(' ')) for s in ann]
    ann = np.array(ann).reshape(2, 2)

    _, ax = plt.subplots(figsize=(3, 3))
    ax.matshow(data, cmap=cm, alpha=1)

    # Add annotations
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            ax.text(
                x=j,
                y=i,
                s=ann[i, j],
                va='center',
                ha='center',
                fontsize=11,
                fontfamily='serif',
            )

    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks(np.arange(len(class_names)))
    ax.set_yticks(np.arange(len(class_names)))
    ax.set_xticklabels(class_names, fontsize=11, fontfamily='serif')
    ax.set_yticklabels(class_names, fontsize=11, fontfamily='serif')
    ax.set_xlabel('Predicted class', fontsize=11, fontfamily='serif')
    ax.set_ylabel('True class', fontsize=11, fontfamily='serif')
    plt.title('Confusion Matrix', fontsize=12, fontweight='bold', fontfamily='serif')
