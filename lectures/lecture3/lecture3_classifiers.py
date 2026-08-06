"""
Helper functions for lecture 3, sections on classifiers.
"""

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np


def plot_classes(X, y, X_test=None, y_test=None):
    """
    Plot classes in y for given features X. Optionally visualize
    training and test data separately, if test data is provided.

    Parameters
    ----------
    X : array-like of shape (n_samples, 2)
        Features x1 and x2
    y : array-like of shape (n_samples,)
        Response variable
    X_test : array-like of shape (n_samples, 2), optional
        Test features x1 and x2
    y_test : array-like of shape (n_samples,), optional
        Test response variable
    """
    fig, ax = plt.subplots(figsize=(4, 4))

    # Indicator whether test data is provided
    has_test = X_test is not None

    colors = ['steelblue', 'darkred']
    markers = ['o', '*']

    classes = np.unique(y)

    for i in classes:
        mask = y == i
        label = f'Class {i} (training)' if has_test else f'Class {i}'
        ax.scatter(
            X[mask, 0],
            X[mask, 1],
            s=50,
            marker=markers[i],
            c=colors[i],
            alpha=0.7,
            lw=0.75,
            label=label,
        )

        if has_test:
            mask = y_test == i
            label = f'Class {i} (test)'
            ax.scatter(
                X_test[mask, 0],
                X_test[mask, 1],
                s=60,
                marker=markers[i],
                c='none',
                edgecolors=colors[i],
                alpha=1.0,
                lw=1.1,
                label=label,
            )

    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    fig.legend(loc='upper left', ncols=1, bbox_to_anchor=(0.92, 0.89))

    return ax


def plot_decision_boundary(ax, x, classifier):
    """
    Plot decision boundary of a classifier on a given axes object.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    x : array-like
        Grid points for x1 and x2.
    classifier : object
        Classifier object used to predict decision boundary.

    """

    xx1, xx2 = np.meshgrid(x, x)

    X = np.column_stack((xx1.ravel(), xx2.ravel()))
    y_pred = classifier.predict(X)
    y_pred = y_pred.reshape(xx1.shape)

    colors = ['steelblue', 'darkred']
    cmap = ListedColormap(colors)

    ax.contourf(xx1, xx2, y_pred, cmap=cmap, alpha=0.15, zorder=-10)
    ax.contour(xx1, xx2, y_pred, colors='black', linewidths=0.5, zorder=-5)


def plot_accuracy_validation_curve(
    param_range, train_scores, test_scores, xlabel='Parameter C', log_scale=True
):
    """
    Plot validation curve with training and test scores

    Parameters
    ----------
    param_range : array-like
        Values of the hyperparameter.
    train_scores : array-like of shape (n_params, n_folds)
        Training scores for each parameter value.
    test_scores : array-like of shape (n_params, n_folds)
        Test scores for each parameter value.
    """

    # Compute average and standard deviation of scores across folds
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)

    plt.figure(figsize=(6, 4))
    plt.plot(
        param_range,
        train_mean,
        c='black',
        ls='--',
        label='Training accuracy',
    )
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
        marker='o',
        markersize=4,
        zorder=10,
        label='Validation accuracy',
    )
    plt.fill_between(
        param_range,
        test_mean + test_std,
        test_mean - test_std,
        alpha=0.15,
        color='steelblue',
        lw=0,
    )
    plt.grid(ls=':', alpha=0.25, color='black', zorder=-10)
    if log_scale:
        plt.xscale('log')
    plt.legend()
    plt.xlabel(xlabel)
    plt.ylabel('Accuracy')
    plt.title('Validation curve')

    ymin = min(np.amin(test_mean - test_std), np.amin(train_mean - train_std))
    ymin = np.floor(ymin * 10) / 10
    plt.ylim((ymin, 1.0))


def plot_generic_confusion_matrix():
    """
    Plot generic confusion matrix
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

    fig, ax = plt.subplots(figsize=(3, 3))
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
