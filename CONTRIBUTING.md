<h1 align="center">Contribution Guidelines</h1>

---

<h2 align="center">Eligibility</h2>

A project is eligible to be added to this list if it is:
- **Awesome!** :sunglasses:
    - Research if the stuff you're including is actually awesome.
    - Only put stuff on the list that you or another contributor can personally recommend.
    - You should rather leave stuff out than include too much.
- Well-documented (wiki, descriptive README.md, javadocs or command-line help available).
- Open-source with a [free license](https://www.gnu.org/licenses/license-list.html).
- Actively maintained (no dead projects!).

---

<h2 align="center">Entry Additions</h2>

1. Make sure the entry is [eligible](#eligibility) for this list.
2. Click on the pen icon at the top of the [README](README.md).
3. Add the entry such that it respects alphabetical order within its parent category. It should use the following convention with a [SPDX License Identifier](https://spdx.org/licenses):

<div align="center">
  <table>
    <tr>
      <th>Wiki Available</th> <th>Markdown Format</th>
    </tr>
    <tr>
      <td align="center">✔️</td>
      <td align="center">
        <br />
        <pre lang="markdown">[Project Name](Source Link) - Description. ([Wiki](Wiki Link)) `SPDX License Identifier`</pre>
      </td>
    </tr>
    <tr>
      <td align="center">❌</td>
      <td align="center">
        <br />
        <pre lang="markdown">[Project Name](Source Link) - Description. `SPDX License Identifier`</pre>
      </td>
    </tr>
  </table>
</div>

5. In the description box at the bottom of the page, state what you added.
6. Propose the changes and open a pull request.

---

<h2 align="center">Category & Subcategory Additions</h2>

<p align="center"><i>When creating new <a href="#entry-additions">entries</a>, it may be necessary to create a new category to logcally sort the entry under.</i></p>

1. Make sure there is no existing category underneath the [Library category](README.md#library) that could logically contain the entry.
2. Click on the pen icon at the top of the [README](README.md).
3. Add the category such that it respects alphabetical order amongst the other subcategories. It should use the following convention:

<div align="center">
  <table>
    <tr>
      <th colspan=2>Category Depth</th> <th>Markdown Format</th>
    </tr>
    <tr>
      <td align="center"><b>1</b></td>
      <td align="center"><b>Child</b></td>
      <td align="center">
        <br />
        <pre lang="markdown">### Library Category Name</pre>
      </td>
    </tr>
    <tr>
      <td align="center"><b>2</b></td>
      <td align="center"><b>Grandchild<br />(Child of Child)</b></td>
      <td align="center">
        <br />
        <pre lang="markdown">#### Library Subcategory Name</pre>
      </td>
    </tr>
  </table>
</div>

5. In the description box at the bottom of the page, state what you added.
6. Propose the changes and open a pull request.
