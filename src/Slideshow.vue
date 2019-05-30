<template lang='pug'>
.eg-theme-agrume
  #business-logic.eg-slideshow
    slide(enter="fadeIn", leave="fadeOut")
      h1 Automatic quality control

      h2 Jakub Skałecki @jskalc
      h4.u-text-centered Mindspace, 30.05.2019

    slide(enter="fadeIn", leave="fadeOut")
      h2 About me
      ul(v-if="step === 1")
        li Currently Technical Team Leader at VideoBeat
        li CTO at <a href='https://pvpc.eu'>PvP Center</a>
        li Backend, DevOps, Frontend, GameDev, Machine Learning...
        li Blogger (sometimes)
        li Polyglot programmer, technology enthusiast

    slide(enter="fadeIn", leave="fadeOut", steps="2")
      h2 Quality control
      h3 Definition
      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step > 1")
        blockquote A part of quality management focused on fulfilling quality requirements, in order to reduce or avoid errors

    slide(enter="fadeIn", leave="fadeOut", steps="3")
      h2 Do we really need highest possible quality?
      h3(v-if="step == 1") Well, not always
      ul(v-if="step == 2")
        li Exploratory, POC projects
        li Internal tools
      div(v-if="step == 3")
        h3 On the other hand
        eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut')
          blockquote Some automation of quality checks almost always pays off

    slide(enter="fadeIn", leave="fadeOut", steps="6")
      h2 Main areas of quality checks

      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step === 2")
        h2 features

      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step === 3")
        h2 security

      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step === 4")
        h2 regression

      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step === 5")
        h2 maintainability

      eg-transition.u-text-centered(enter='bounceInLeft', leave='fadeOut', v-if="step === 6")
        h2 performance


    slide(enter="fadeIn", leave="fadeOut")
      h2 Levels of quality control maturity

    slide(enter="fadeIn", leave="fadeOut", steps="3")
      h3 Level 0
      h2(v-if="step > 1") No quality checks at all
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step > 2")
        div.u-text-centered
           img.presentation-image(src="./assets/this-is-fine.jpg", width="100%")

    slide(enter="fadeIn", leave="fadeOut", steps="5")
      h3 Level 1
      h2(v-if="step > 1") Manual verification after release
      ul
        li(v-if="step > 1 && step < 5") After each release manual tests are performed
        li(v-if="step > 2 && step < 5") Small initial cost, but very costly long-term
        li(v-if="step > 3 && step < 5") Most projects are at this level
        eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step > 4")
          div.u-text-centered
            img.presentation-image(src="./assets/manual-testing.jpg")

    slide(enter="fadeIn", leave="fadeOut", steps="5")
      h3 Level 2
      h2(v-if="step > 1 && step < 5") Code review
      ul
        li(v-if="step > 2 && step < 5") Requires 2+ developers
        li(v-if="step > 2 && step < 5") New code has to be approved by another person
        li(v-if="step > 3 && step < 5") Committing directly to the main branch should be <strong>prohibited</strong>
        li(v-if="step > 4 && step < 5") This part can't be automated, but can be made much easier
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step > 4")
          div.u-text-centered
            img.presentation-image(src="./assets/3ksloc.jpg")

    slide(enter="fadeIn", leave="fadeOut", steps="6")
      h3 Level 3
      h2(v-if="step > 1 && step < 6") Local unit & style tests
      ul
        li(v-if="step > 2 && step < 5") Unit tests are created using framework of choice
        li(v-if="step > 3 && step < 5") They are started locally, on demand
        li(v-if="step > 3 && step < 5") Checks for big files, secrets, merge conflicts
        li(v-if="step > 4 && step < 6") Linters: flake8, jslint, checkstyle
        li(v-if="step > 4 && step < 6") Test runners: pytest, jest
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step > 5")
          div.u-text-centered
            img.presentation-image(src="./assets/not-always-write-tests.jpg")

    slide(enter="fadeIn", leave="fadeOut")
      eg-transition(enter='bounceInLeft', leave='fadeOut')
        div.u-text-centered
          img.presentation-image--solo(src="./assets/automate.jpg")

    slide(enter="fadeIn", leave="fadeOut", steps="4")
      h2 Git hooks
      ul
        li(v-if="step > 1 && step < 4") Allows to run a script before commit/push
        li(v-if="step > 1 && step < 4") If script fails, commit / push is prevented
        li(v-if="step > 2 && step < 4") Can be skipped using --no-verify flag
        li(v-if="step > 2 && step < 4") Should be version controlled
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step === 4")
        h3 The easiest automation available!

    slide(enter="fadeIn", leave="fadeOut", steps="7")
      h3 Level 4
      h2(v-if="step > 1") Automated local tests
      ul
        li(v-if="step > 2") Not manual anymore, started automatically
        li(v-if="step > 3") Fast feedback
        li(v-if="step > 4") After being configured once, usually no changes are needed
        li(v-if="step > 5") Can be run "on save" or as pre-commit / pre-push git hooks
        li(v-if="step > 6") Tools: git, pre-commit

    slide(enter="fadeIn", leave="fadeOut", steps="5")
      h3 Level 5
      h2(v-if="step > 1 && step < 5") Automatic fixing style violations
      ul
        li(v-if="step > 2 && step < 5") Manual fixing of code is highly repetitive
        li(v-if="step > 2 && step < 5") Direct improvement over previous step
        li(v-if="step > 3 && step < 5") Tools: Code autoformatters (prettier, black)
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step === 5")
        h2 Most projects should reach this level

    slide(enter="fadeIn", leave="fadeOut", steps="5")
      h3 Level 6
      h2(v-if="step > 1 && step < 5") Continous Integration server
      ul
        li(v-if="step > 2 && step < 5") CI server running & enforcing successful build / tests pass
        li(v-if="step > 2 && step < 5") It should be impossible to merge branch not passing tests
        li(v-if="step > 3 && step < 5") Tools: Jenkins, Travis, Bitbucket pipelines, Gitlab runner
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step === 5")
        div.u-text-centered
          img.presentation-image--solo(src="./assets/ci.png")

    slide(enter="fadeIn", leave="fadeOut", steps="6")
      h3 Level 7
      h2(v-if="step > 1") Calculation of various code metrics
      ul
        li(v-if="step > 2") Test coverage
        li(v-if="step > 3") Maintainability Index
        li(v-if="step > 4") Cyclomatic Complexity
        li(v-if="step > 5") Tools: codeclimate, sonarqube

    slide(enter="fadeIn", leave="fadeOut", steps="4")
      h3 Level 8
      h2(v-if="step > 1") Dependency scanning & license management
      ul
        li(v-if="step > 2") Find vulnerabilities in used packages
        li(v-if="step > 3") Check license compliance (avoid "viral" licenses, like GPL)

    slide(enter="fadeIn", leave="fadeOut", steps="8")
      h3 Level 9++
      h2(v-if="step > 1") Higher level tests
      ul
        li(v-if="step > 2 && step < 8") Static / dynamic security testing
        li(v-if="step > 3 && step < 8") Smoke tests
        li(v-if="step > 4 && step < 8") End to End tests
        li(v-if="step > 5 && step < 8") Performance tests
        li(v-if="step > 6 && step < 8") Tools: selenium, locust, vegetta
      eg-transition(enter='bounceInLeft', leave='fadeOut', v-if="step === 8")
        div.u-text-centered
          img.presentation-image(src="./assets/smoke-testing.jpeg")

    slide(enter="fadeIn", leave="fadeOut")
      h2 Summary
      h3 Higher you are, faster you move
      h3 But first calculate ROI

    slide(enter="fadeIn", leave="fadeOut")
      h2 Live demo
      eg-transition(enter='bounceInLeft', leave='fadeOut')
        div.u-text-centered
          img.presentation-image(src="./assets/live-demo.jpg")

    slide(enter="fadeIn", leave="fadeOut")
      h2 Thank you!
      h3 Questions?

</template>

<script>
import eagle from 'eagle.js'

export default {
  mixins: [ eagle.slideshow ],
  components: {},
  data () {
    return {
      shortVersion: true
    }
  }
}
</script>

<style lang='scss'>
  @import url(https://fonts.googleapis.com/css?family=Oxygen);
  #business-logic {
    //background-image: url("~eagle.js/dist/themes/assets/crossword.png");

    &.eg-slideshow::after {
      content: "@jskalc";
      padding-right: 45px;
      padding-top: 3px;
      position: absolute;
      font-size: 0.8em;
      right: 20px;
      bottom: 20px;
      background: url(./assets/twitter.png) no-repeat right;
      background-size: contain;
    }

    &.eg-slideshow::before {
      content: "Valian";
      position: absolute;
      padding-left: 45px;
      padding-top: 5px;
      font-size: 0.8em;
      left: 20px;
      bottom: 20px;
      color: #0e3d54;
      background: url(https://image.flaticon.com/icons/svg/25/25231.svg) no-repeat;
      background-size: contain;
    }

    h1, h2, h3, h4, div, blockquote, p, ul, li {
      font-family: "Oxygen", sans-serif;
      color: #184555;
    }

    h1 { font-size: 3.2em; color: #184555; }
    h2 { font-size: 2.1em; }
    h3 { font-size: 1.5em; text-transform: none;}
    h4 { font-size: 1.2em; }
    blockquote {
      font-style: italic;
    }
    ul li {
      margin-bottom: 0.3em;
    }
    .eg-code-block {
      font-size: 0.6em;
    }

    .presentation-image {
      &--solo {
        margin: 15% auto;
      }
    }
  }
  .u-text-centered {
    text-align: center;
  }
</style>
